import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';
import {GlobalVariable} from './global';
import {ConverterService} from './../shared/converter.service';



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
  message!: any;
  dispBool!: boolean;
  subscription!: Subscription;
  height!: any;
  width!: any;

  private globalFilterVar = GlobalVariable.globalVar;
  
  constructor(private imgData: ComponentCommunicationService,private trackerService: ConverterService ) { }

  ngOnInit(): void {
    //subscribe for communication between components
    this.subscription = this.imgData.currentMessage.subscribe(message => this.message = message);
    this.subscription = this.imgData.currentDisplayDownload.subscribe(dispBool => this.dispBool = dispBool);
    this.subscription = this.imgData.currentHeight.subscribe(height => this.height = height);
    this.subscription = this.imgData.currentWidth.subscribe(width => this.width = width);
    console.log("Filter"+this.height);
    console.log("Filter"+this.width);
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }


  original(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "revert"
    this.globalFilterVar = "revert";
    this.imgData.changeFilter("revert");
  }

  grayScale(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "grayscale(100%)"
    this.globalFilterVar = "grayscale";
    this.imgData.changeFilter("grayscale");
  }

  sepia(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "sepia(100%)"
    this.globalFilterVar = "sepia";
    this.imgData.changeFilter("sepia");
  }

  contrast(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "contrast(200%)"
    this.globalFilterVar = "contrast";
    this.imgData.changeFilter("contrast");
  }

  hueRotate(){
    var x=document.getElementById("imgLink") as HTMLLinkElement
    x.style.filter = "hue-rotate(90deg)"
    this.globalFilterVar = "hueRotate";
    this.imgData.changeFilter("hueRotate");
  }

  //downloadFile is used to download an image
  downloadFile() {
    var a = document.createElement('a');
    a.href = this.message.image;
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
    else if(this.globalFilterVar == "sepia"){
      filterVar = "sepia";
    }
    else if(this.globalFilterVar == "contrast"){
      filterVar = "contrast";
    }
    else if(this.globalFilterVar == "hueRotate"){
      filterVar = "hueRotate";
    }
    else if(this.globalFilterVar == "revert"){
      filterVar = "revert";
    }

    myTest(imgBckend,filterVar);
    
  }
  // used to save the image in png format
  downloadPngFile()
  {
    var a = document.createElement('a');
    a.href = this.message.image;
    // myTest(a.href,this.filter,"jpg");
    
    this.incrementDownload();
    a.href = this.message.jpg;
    var imgBckend = a.href;
    a.download = "output.png";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }
  
  upload(){
    //  uploadImage(window.event);
    myTest();
  }
// used to increment stats of download
  incrementDownload()
  {
    
    this.trackerService.activityTrackerIncrement("Downloads").subscribe(
      responseData =>{
            //response
            console.log(responseData);
           
        }
    );
  }
}