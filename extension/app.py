import os
import threading
import queue
from flask import Flask, render_template, request, jsonify
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

app = Flask(__name__)

audio_queue = queue.Queue()

recording_in_progress = False
from google.cloud import speech_v1p1beta1 as speech

def transcribe_realtime(audio_data):
    client = speech.SpeechClient()

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )
    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    requests = [
        speech.StreamingRecognizeRequest(audio_content=chunk)
        for chunk in audio_data
    ]

    try:
        responses = client.streaming_recognize(streaming_config, requests)

        for response in responses:
            for result in response.results:
                print("Transcript: {}".format(result.alternatives[0].transcript))
    except Exception as e:
        print(f"Error during transcription: {str(e)}")

def record_audio():
    global recording_in_progress
    recording_in_progress = True

    duration = 10  
    fs = 44100  
    channels = 2  

    with sd.InputStream(samplerate=fs, channels=channels):
        print("Recording started...")
        audio_data = sd.rec(int(duration * fs), dtype='int16')
        sd.wait()
        print("Recording stopped...")

    recording_in_progress = False

    
    transcribe_realtime(audio_data)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/start_recording', methods=['POST'])
def start_recording():
    global recording_thread
    if not recording_in_progress:
        recording_thread = threading.Thread(target=record_audio)
        recording_thread.start()
    return 'Recording started'

@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    global recording_in_progress
    if recording_in_progress:
        recording_thread.join()  
    return 'Recording stopped'

@app.route('/get_text', methods=['GET'])
def get_text():
    full_text = ""
    while not audio_queue.empty():
        filename = audio_queue.get()
        text = transcribe_realtime(filename)
        full_text += text + " "
    return jsonify({"text": full_text})


from flask import Flask, render_template, request
from transformers import M2M100ForConditionalGeneration, AutoTokenizer, pipeline

app = Flask(__name__)

model_name = "facebook/m2m100_418M"
translator_model = M2M100ForConditionalGeneration.from_pretrained(model_name)
translator_tokenizer = AutoTokenizer.from_pretrained(model_name)

supported_languages = ["en", "hi", "kn", "mr", "pa", "ur", "ta", "ml", "bn", "sn"]

@app.route("/")
def index():
    return render_template("index1.html", languages=supported_languages)

@app.route("/process", methods=["POST"])
def process():
    user_input = request.form["user_input"]
    input_language = request.form["input_language"]
    target_language = request.form["target_language"]

    model_inputs = translator_tokenizer(user_input, return_tensors="pt")
    gen_tokens = translator_model.generate(**model_inputs, forced_bos_token_id=translator_tokenizer.get_lang_id(target_language))
    translated_text = translator_tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)[0]


    return render_template("index1.html", user_input=user_input, translated_text=translated_text,languages=supported_languages, input_language=input_language)


if __name__ == "__main__":
    app.run(debug=True, port = 4000)