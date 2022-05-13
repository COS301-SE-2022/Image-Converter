import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.scss']
})
export class FilterComponent implements OnInit {

  //these variables are used for the communication between converter and filter components
  message!: string;
  subscription!: Subscription;
  
  constructor(public sanitizer: DomSanitizer,private imgData: ComponentCommunicationService) { }

  ngOnInit(): void {
    //subscribe for communication between components
    this.subscription = this.imgData.currentMessage.subscribe(message => this.message = message);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
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

  //downloadFile is used to download an image
  downloadFile() {
    var a = document.createElement('a');
  a.href = this.message;
  a.download = "output.png";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  }
}
