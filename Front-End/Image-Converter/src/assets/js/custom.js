function myTest(imgBckend,filterVar,imgFormat = "png"){
var img = new Image();
img.crossOrigin = ""; 
img.onload = draw; 
img.src = imgBckend;

function  draw() {
  var canvas = document.querySelector("canvas"),
      ctx = canvas.getContext("2d");

  canvas.width = this.width;
  canvas.height = this.height;
  console.log(filterVar);
  
  // filter
  if (typeof ctx.filter !== "undefined") {
    if(filterVar==="grayscale"){
      ctx.filter = "grayscale(1.0)";
      ctx.drawImage(this, 0, 0);
    }
    else if(filterVar==="sepia"){
      ctx.filter = "sepia(1.0)";
      ctx.drawImage(this, 0, 0);
    }
    else if(filterVar==="contrast"){
      ctx.filter = "contrast(2.0)";
      ctx.drawImage(this, 0, 0);
    }
    else if(filterVar==="hueRotate"){
      ctx.filter = "hue-rotate(90deg)";
      ctx.drawImage(this, 0, 0);
    }
    else if(filterVar==="revert" || filterVar==undefined){
      ctx.filter = "revert";
      ctx.drawImage(this, 0, 0);
    }
    
  }
  else {
    
  }
  var dataURL = canvas.toDataURL();

  var dlnk;
  if(imgFormat=="png")
  {
    dlnk=document.getElementById('dwnldLnk');
  }
  else
  {
    dlnk=document.getElementById('dwnldLnk2');
  }
   
  var pdf = dataURL;
  dlnk.href = pdf;
  dlnk.click();


	}

}

