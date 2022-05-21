import { Component } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {


// constructor(public sanatizer: DomSanitizer) {}

ngOnInit(): void {  
}

  // w3_open() {
  //   document.getElementById("mySidebar").style.display = "block";
  //   document.getElementById("myOverlay").style.display = "block";
  // }
   
  // w3_close() {
  //   document.getElementById("mySidebar").style.display = "none";
  //   document.getElementById("myOverlay").style.display = "none";
  // }


  
  //  original(){
  //   var x=document.getElementById("imgLink") as HTMLLinkElement
  //   x.style.filter = "revert"
  // }
  
  //  grayScale(){
  //   var x=document.getElementById("imgLink") as HTMLLinkElement
  //   x.style.filter = "grayscale(100%)"
    
  // }
  
  //  sepia(){
  //   var x=document.getElementById("imgLink") as HTMLLinkElement
  //   x.style.filter = "sepia(100%)"
  // }
  
  //  contrast(){
  //   var x=document.getElementById("imgLink") as HTMLLinkElement
  //   x.style.filter = "contrast(200%)"
  // }
  
  //  hueRotate(){
  //   var x=document.getElementById("imgLink") as HTMLLinkElement
  //   x.style.filter = "hue-rotate(90deg)"
  // }
}


// function downdloadFile() {
//   myTest();
// }

// function original(){
//   var x=document.getElementById("imgLink") as HTMLLinkElement
//   x.style.filter = "revert"
// }

// function grayScale(){
//   var x=document.getElementById("imgLink") as HTMLLinkElement
//   x.style.filter = "grayscale(100%)"
  
// }

// function sepia(){
//   var x=document.getElementById("imgLink") as HTMLLinkElement
//   x.style.filter = "sepia(100%)"
// }

// function contrast(){
//   var x=document.getElementById("imgLink") as HTMLLinkElement
//   x.style.filter = "contrast(200%)"
// }

// function hueRotate(){
//   var x=document.getElementById("imgLink") as HTMLLinkElement
//   x.style.filter = "hue-rotate(90deg)"
// }

