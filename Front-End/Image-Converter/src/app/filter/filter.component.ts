import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';
import { image } from 'html2canvas/dist/types/css/types/image';
import { ReturnStatement } from '@angular/compiler';
import {GlobalVariable} from './global'

declare const myTest:any;
declare const uploadImage:any;
// declare var temp: any;


@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.scss']
})
export class FilterComponent implements OnInit {

  //these variables are used for the communication between converter and filter components
  message!: string;
  dispBool!: boolean;
  subscription!: Subscription;
  private globalFilterVar = GlobalVariable.globalVar;
  
  constructor(public sanitizer: DomSanitizer,private imgData: ComponentCommunicationService ) { }

  ngOnInit(): void {
    //subscribe for communication between components
    this.subscription = this.imgData.currentMessage.subscribe(message => this.message = message);
    this.subscription = this.imgData.currentDisplayDownload.subscribe(dispBool => this.dispBool = dispBool);
    
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
    this.globalFilterVar = "grayscale";
    
  }

  sepia(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "sepia(100%)"
    this.globalFilterVar = "grayscale";
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
    var imgBckend = a.href;
  // a.download = "output.png";
  // document.body.appendChild(a);
  // a.click();
  // document.body.removeChild(a);
var filterVar;
// console.log(temp);
  if(this.globalFilterVar == "grayscale"){
    filterVar = "grayscale";
  }

  myTest(imgBckend,filterVar);
  // alert(myTest);

  }

 upload(){
  //  uploadImage(window.event);
  myTest();
 }



}

