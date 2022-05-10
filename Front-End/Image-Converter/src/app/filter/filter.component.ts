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

  grayScale(){
    //alert("Moe")
    var x=document.getElementById("linnk") as HTMLLinkElement
    x.style.filter = "grayscale(100%)"
  }

}
