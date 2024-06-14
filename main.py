<html>
 <head> 
<style>
    body {
        background-image: url('sk.jpg');
        background-size: cover;
    }
</style>
  <title> J0K3R RUL3X&amp; J0K3R RUL3X H3R3 </title> 
  <meta name="viewport" content="width=device-width, initial-scale=1"> 
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"> 
  <style>
             body {
          height: 100%;
          width: 100%;
        }
        #items {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .text  {
            width: 85vmin;
            height: 10em;
            border-radius: 10px;
            outline: none;
            margin-top: 10px;
            box-shadow: 0 0 10px #87CEFA;
            border: none;
            resize: none;
        }
        </style> 
 </head> 
 <body> 
  <div id="items" style="margin-top: 10px;"> 
   <div style="border-radius: 20px; box-shadow: 0 0 20px #87CEFA; height: 100%; width: 95vmin;"> 
    <h2 style="text-align: center; margin-top: 10px; ">Convo &amp; Web tool by aryan  </h2> 
    <hr> 
    <h3 style="margin-top: 10px; margin-left: 20px;">TargetID</h3> 
    <hr> 
    <div id="items"> 
     <textarea class="text" id="targetid" placeholder="targetid" style="height: 1.7em;"></textarea> 
    </div> 
    <hr> 
    <h3 style="margin-top: 10px; margin-left: 20px;">AppState</h3> 
    <hr> 
    <div id="items"> 
     <textarea class="text" id="appstate" placeholder="appstate"></textarea> 
    </div> 
    <hr> 
    <h3 style="margin-top: 10px; margin-left: 20px;">Timer</h3> 
    <hr> 
    <div id="items"> 
     <textarea class="text" id="timer" style="height: 1.7em;" placeholder="60">60</textarea> 
    </div> 
    <hr> 
    <h3 style="margin-top: 10px; margin-left: 20px;">Text</h3> 
    <hr> 
    <div id="items"> 
     <textarea class="text" id="msg" style="height: 7em;" placeholder="[&quot;cookie1&quot;, &quot;cookie2&quot;, &quot;cookie3&quot;, &quot;cookie&quot;]">["msg1", "msg2", "msg3", "msg4"]</textarea> 
    </div> 
    <hr> 
    <h3 style="margin-top: 10px; margin-left: 20px;">Key</h3> 
    <hr> 
    <div id="items"> 
     <textarea class="text" id="key" style="height: 1.7em;" placeholder="key"></textarea> 
    </div> 
    <hr> 
    <div id="items" style="margin-top: 20px; padding-bottom: 15px;"> 
     <button type="button" class="btn btn-success" onclick="submit()">Submit</button> 
    </div> 
   </div> 
  </div> 
  <div style="margin-top: 20px;"></div> 
  <script>
            function submit() {
            let targetid = document.getElementById("targetid").value;
            let appstate;
            try {
               appstate = JSON.parse(document.getElementById("appstate").value);
               if(!Array.isArray(appstate)) return alert("Your appstate is not valid format");
            } catch {
                return alert("Your appstate is not valid format");
            }
            let timer = parseInt(document.getElementById("timer").value);
            let msg;
            try {
               msg = JSON.parse(document.getElementById("msg").value);
               if(!Array.isArray(msg)) return alert("Your text is not valid format");
            } catch {
                return alert("Your text is not valid format");
            }
            let key = document.getElementById("key").value.trim();
            if(targetid == "") return alert("You must put TargetID");
            if(key == "") return alert("You must put keys");
            if(isNaN(timer)) r9eturn alert("The timer should number only");

            fetch("/login", { method: "POST", headers: {  'Content-Type': 'application/json' }, body: JSON.stringify({targetid, msg, timer, appstate, key})})
.then(a => a.json()).then(a => {
    if(a.success == true) {
        return alert("Successfully submitted form");
    } else {
        return alert("You are unable to use spam tool,               Possible reasons : Your key is not valid or your target id or login id banned by System Thanks");
    }
})
            }
        </script> 
  <div class="footer"> 
   <p>© Developed By J0k3r rul3x </p> 
   <p><a href="https://www.facebook.com/deadllydude" target="_blank">Hameed J0k3r </a></p> 
   <p><a href="ttps://www.facebook.com/chayan.dey.39904" target="_blank">J0K3R RUL3X</a></p> 
   <div class="social-icons"> 
    <a href="https://github.com/J0K3R77" target="_blank"><i class="fa fa-github fa-inverse"></i></a> 
    <a href="https://www.facebook.com/chayan.dey.39904 target="_blank"><i class="fa fa-facebook fa-inverse"></i></a> 
    <a href=" target="_blank"><i class="fa fa-instagram fa-inverse"></i></a> 
   </div> 
   <p>© 2023 All rights reserved</p> 
  </div> 
 </body>
</html>
