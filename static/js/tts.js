
function tts() {
    let action = document.querySelector("#tts").innerHTML;
    if(action == "Play") {
      if ('speechSynthesis' in window) {
        var msg = new SpeechSynthesisUtterance();
        msg.text = document.querySelector("#content").innerHTML;
        window.speechSynthesis.speak(msg);
       }else{
         alert("Sorry, your browser doesn't support text to speech!");
       }
      document.querySelector("#tts").innerHTML = "Stop";
    }else{
      window.speechSynthesis.cancel();
      document.querySelector("#tts").innerHTML = "Play";
    }
  }