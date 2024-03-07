chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === "start_recording" || request.message === "stop_recording" || request.message === "get_text") {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
          var activeTab = tabs[0];
          chrome.tabs.sendMessage(activeTab.id, { message: request.message });
      });
  }
});
