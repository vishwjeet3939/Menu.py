#!/usr/bin/python36

print("content-type: text/html")
print()
		
print("""
<html>
<head>
<title>Home</title>
<style>
   body
   {
     background-color: black;
     margin: 0;
    }

  .navbar
  {
    text-decoration: none;
    border: solid;
    border-width: 0px;
    padding: 0px;
    background-color: #0f0f20;
    font-size: 30px;
    margin-left: 0px;
    color: pink;
  }

  .navbar:hover
  {
   color: blue;
   background-color: black; 
  }

  #navbar
  {
    background-color: orange;
    color: black;
    position: relative;
  }

  .mic
  {
   background-color: pink;
   border: solid;
   border-radius: 25%;
   position: relative;
   left: 200px;
  }
  

  button:focus
  {
   outline: none;
   }

  #voicebox
   {
    position: absolute;
    top: 350px;
    left: 510px;
    border: solid;
    }

   #speak
   {
    width: 500px;
   }
</style>

<script>
        window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
        let finalTranscript = '';
        let recognition = new window.SpeechRecognition();
        recognition.interimResults = true;
        recognition.maxAlternatives = 10;
        recognition.continuous = true;  
        recognition.onresult = (event) => {
        let interimTranscript = '';
        for (let i = event.resultIndex, len = event.results.length; i < len; i++) {
            let transcript = event.results[i][0].transcript;
            if (event.results[i].isFinal) {  
            finalTranscript += transcript;
            } else {
            interimTranscript += transcript;
            }
        }
        
        document.getElementById('speak').value = finalTranscript + interimTranscript ;
       
    }
   var x = 0;
    function count(){
     x = x + 1 ;
     task();
  }
    
  function task(){
      if (x%2 != 0){
          document.getElementById('m').style.backgroundColor = 'green'; 
          recognition.start();
      }
      else if (x%2 == 0){
          document.getElementById('m').style.backgroundColor = 'red';
          recognition.stop();
          document.getElementById('speak').value = 'Recording stopped';
      }
  }

</script>
</head>
<body>
   <div id='voicebox'>
   <button id='m' class='mic' onclick='count()'><img id='mic' width=40px height=40px src='http://192.168.43.239/mic.png' ></img></button></br>
<form action="http://192.168.43.64/cgi-bin/cmdproc.py">
<input type="text" id="speak" name="cmd"/>
<input type="reset"/>
<input type="submit"/>
</form>
</div> 
</body>

</html>

""")
