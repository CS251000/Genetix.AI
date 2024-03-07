chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === "start_recording") {
      // Perform actions when start recording message is received
      console.log("Start recording...");

      // Your custom logic for starting recording goes here
  } else if (request.message === "stop_recording") {
      // Perform actions when stop recording message is received
      console.log("Stop recording...");

      // Your custom logic for stopping recording goes here
  } else if (request.message === "get_text") {
      // Perform actions when get text message is received
      console.log("Getting text...");

      // Your custom logic for retrieving text goes here
      var retrievedText = "This is the retrieved text.";  // Replace with your actual logic

      // Send the retrieved text back to the popup
      sendResponse({ text: retrievedText });
  }
});
