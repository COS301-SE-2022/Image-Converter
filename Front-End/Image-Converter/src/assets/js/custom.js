function myTest(){
var img = new Image();
img.crossOrigin = ""; 
img.onload = draw; 
img.src = "https://image.shutterstock.com/image-photo/bright-purple-pink-sky-beautiful-260nw-1704295576.jpg";


function  draw() {
  var canvas = document.querySelector("canvas"),
      ctx = canvas.getContext("2d");

  canvas.width = this.width;
  canvas.height = this.height;
  
  // filter
  if (typeof ctx.filter !== "undefined") {
    ctx.filter = "sepia(0.8)";
    ctx.drawImage(this, 0, 0);
  }
  else {
    // ctx.drawImage(this, 0, 0);
    // TODO: manually apply filter here.
  }
  var dataURL = canvas.toDataURL();

  var dlnk = document.getElementById('dwnldLnk');
  var pdf = dataURL;
  dlnk.href = pdf;
  dlnk.click();


	}

}

