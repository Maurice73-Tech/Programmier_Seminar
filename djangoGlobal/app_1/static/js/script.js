// Google Web Speech API for using mic
var speechRecognition = window.webkitSpeechRecognition

var recognition = new speechRecognition()

var searchInput = $("#searchInput")

var instructions = $("#instructions")

var content = ''

recognition.continuous = true

// recognition is started

// not used anymore
recognition.onstart = function () {
  instructions.text("Spracherkennung ist eingeschaltet")
}

recognition.onspeechend = function(){
  recognition.stop()
  // not used anymore
  instructions.text("Spracherkennung ist ausgeschaltet")

}

recognition.onerror = function() {
  // not used anymore
  instructions.text("Noch einmal versuchen")
}

recognition.onresult = function(event) {
  var current = event.resultIndex
  var transcript = event.results[current][0].transcript

  content = transcript

  searchInput.val(content)
  //$("#searchInput").trigger(e);
}

$("#start-btn").click(function (event) {
  if (content.length) {
    content += ''
  }

  recognition.start()
  //$("#searchInput").trigger($.Event("keypress", { keyCode: 13 }));
})

$("#stop-btn").click( function (event) {
  recognition.stop()
  //$("#searchInput").val('')
})

searchInput.on('input', function() {
  content = $(this).val()
})