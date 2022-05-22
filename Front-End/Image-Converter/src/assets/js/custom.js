function myTest(imgBckend,filterVar){
var img = new Image();
img.crossOrigin = ""; 
img.onload = draw; 
img.src = imgBckend;

function  draw() {
  var canvas = document.querySelector("canvas"),
      ctx = canvas.getContext("2d");

  canvas.width = this.width;
  canvas.height = this.height;
  
  // filter
  if (typeof ctx.filter !== "undefined") {
    if(filterVar==="grayscale"){
      ctx.filter = "grayscale(1.0)";
      ctx.drawImage(this, 0, 0);

    }
  }
  else {
    console.log("else")
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

