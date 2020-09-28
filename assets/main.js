const electron = require("electron");
const ipcRenderer = electron.ipcRenderer;

function FileChanged(){
  reRead();
  setInterval("reRead()", 1000);
}

function reRead() {
  var fileRef = document.getElementById('selectFile');
  if (1 <= fileRef.files.length) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET",fileRef.files[0]["path"],true);
    xmlHttp.send(null);
    xmlHttp.onload = function(){
        var data = xmlHttp.responseText;
        console.log(data);
        document.getElementById('main-textarea').value = data;
        document.getElementById("main-textarea").scrollTop = document.getElementById("main-textarea").scrollHeight
    }
  }
}

function Close() {
  console.log("usu!");
  ipcRenderer.send('close-message', 'close');
}
