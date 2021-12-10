var speechRecognition = window.webkitSpeechRecognition

var recognition = new speechRecognition()

var searchInput = $("#searchInput")

var instructions = $("#instructions")

var content = ''

recognition.continuous = true

// recognition is started

recognition.onstart = function () {
  instructions.text("Spracherkennung ist eingeschaltet")
}

recognition.onspeechend = function(){
  recognition.stop()
  instructions.text("Spracherkennung ist ausgeschaltet")

}

recognition.onerror = function() {
  instructions.text("Noch einmal versuchen")
}

recognition.onresult = function(event) {
  var current = event.resultIndex
  var transcript = event.results[current][0].transcript

  content = transcript

  searchInput.val(content)

}

$("#start-btn").click(function (event) {
  if (content.length) {
    content += ''
  }

  recognition.start()

})

$("#stop-btn").click( function (event) {
  recognition.stop()
  //$("#searchInput").val('')
})

searchInput.on('input', function() {
  content = $(this).val()
})