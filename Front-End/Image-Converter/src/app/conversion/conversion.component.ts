import { Component, OnInit } from '@angular/core';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import {ConverterService} from './../shared/converter.service';
import { Subscription } from 'rxjs';
//import {GlobalVariable} from './global';

declare const myTest:any;

@Component({
  selector: 'app-conversion',
  templateUrl: './conversion.component.html',
  styleUrls: ['./conversion.component.scss']
})
export class ConversionComponent implements OnInit {

  //these variables are used for the communication between converter and filter components
  message!: any;
  message2!: any;
  dispBool!: boolean;
  subscription!: Subscription;

  filter!:any;
  constructor(private imgData: ComponentCommunicationService,private trackerService: ConverterService) { }

  ngOnInit(): void {
    //subscribe for communication between components
    this.subscription = this.imgData.currentMessage.subscribe(message => this.message = message);
    this.subscription = this.imgData.currentimgFilter.subscribe(filter => this.filter = filter);
    this.subscription = this.imgData.currentDisplayDownload.subscribe(dispBool => this.dispBool = dispBool);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
   //download png function
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

  //download jpg function
  downloadJpgFile()
  {
    var a = document.createElement('a');
    console.log(this.message);

    a.href = this.message.image;
    // myTest(a.href,this.filter,"jpg");

    this.incrementDownload();
    a.href = this.message.jpg;
    var imgBckend = a.href;
    a.download = "output.jpg";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  //download TIFF function
  downloadTIFFFile()
  {
    var a = document.createElement('a');
    console.log("TIFF: "+ this.message.tiff);

    a.href = this.message.image;
    // myTest(a.href,this.filter,"jpg");

    this.incrementDownload();
    a.href = this.message.tiff;
    var imgBckend = a.href;
    a.download = "output.tiff";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  downloadBMPFile() {
    var a = document.createElement('a');
    console.log("BMP: "+ this.message.bmp);

    a.href = this.message.image;
    // myTest(a.href,this.filter,"jpg");

    this.incrementDownload();
    a.href = this.message.bmp;
    var imgBckend = a.href;
    a.download = "output.bmp";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  downloadSVGFile() {
    var a = document.createElement('a');
    console.log("BMP: "+ this.message.bmp);

    a.href = this.message.image;
    // myTest(a.href,this.filter,"jpg");

    this.incrementDownload();
    a.href = this.message.svg;
    var imgBckend = a.href;
    a.download = "output.svg";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  //tracks number of downloads
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
