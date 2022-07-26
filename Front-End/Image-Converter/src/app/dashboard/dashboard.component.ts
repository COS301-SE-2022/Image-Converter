import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  
  }

  toHome() {
    var x = document.getElementById("home") as HTMLLinkElement
    x.scrollIntoView();
  }
  toImageUpload(){
    var x = document.getElementById("imageUpload") as HTMLLinkElement
    x.scrollIntoView();
  }
  // toImageFilter(){
  //   var x = document.getElementById("imageFilter") as HTMLLinkElement
  //   x.scrollIntoView();
  // }
  toConversionFormat(){
    var x = document.getElementById("conversionFormat") as HTMLLinkElement
    x.scrollIntoView();
  }
  toUploadHistory(){
    var x = document.getElementById("uploadHistory") as HTMLLinkElement
    x.scrollIntoView();
  }
  toContact(){
    var x = document.getElementById("contact") as HTMLLinkElement
    x.scrollIntoView();
  }
  toGraphVis(){
    var x = document.getElementById("graphVis") as HTMLLinkElement
    x.scrollIntoView();
  }

}


