import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.scss']
})
export class FilterComponent implements OnInit {
  constructor(public sanitizer: DomSanitizer) { }

  ngOnInit(): void {
  }

  original(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "revert"
  }

  grayScale(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "grayscale(100%)"
  }

  sepia(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "sepia(100%)"
  }

  contrast(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "contrast(200%)"
  }

  hueRotate(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "hue-rotate(90deg)"
  }

}
