import { Component, OnInit } from '@angular/core';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';

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

  constructor(private imgData: ComponentCommunicationService) { }

  ngOnInit(): void {
    //subscribe for communication between components
    this.subscription = this.imgData.currentMessage.subscribe(message => this.message = message);
    this.subscription = this.imgData.currentDisplayDownload.subscribe(dispBool => this.dispBool = dispBool);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
   //download png function
  downloadPngFile()
  {
    var a = document.createElement('a');
    a.href = this.message.png;
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
    console.log("jpeg: "+this.message.jpg);
    a.href = this.message.jpg;
    var imgBckend = a.href;
    a.download = "output.jpg";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }
}