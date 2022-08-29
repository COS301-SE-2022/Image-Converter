import { Component, OnInit } from '@angular/core';
// // import {Desmos} from 'desmos';
import html2canvas from 'html2canvas';
import {ConverterService} from './../shared/converter.service';
// declare var Desmos: any;

@Component({
  selector: 'app-live-graphing2',
  templateUrl: './live-graphing2.component.html',
  styleUrls: ['./live-graphing2.component.scss']
})

export class LiveGraphing2Component implements OnInit {
  myScriptElement: HTMLScriptElement;
  Desmos: any;
  

  constructor(private  graphService: ConverterService) { 
    this.myScriptElement = document.createElement("script");
    this.myScriptElement.src = "https://www.desmos.com/api/v1.7/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6";
    document.body.appendChild(this.myScriptElement);

  }

  calculator:any;

  ngOnInit(): void {

      this.myScriptElement.onload = () => {
        this.Desmos = (<any>window).Desmos;
        console.log('loaded');
        document.getElementsByTagName('head')[0].appendChild(this.myScriptElement);
        var elt = document.getElementById('calculator');
        // var calculator = this.Desmos.GraphingCalculator(elt, { keypad: true, expressions: true, settingsMenu: false, expressionsCollapsed: true });
        this.calculator = this.Desmos.GraphingCalculator(elt);      
        this.calculator.setExpression({});
         
    }

    // alert("hey");

  }

  //saves plotted graph
   captureScreenshots() {
    var containerElt = document.getElementById('screenshot-container');
    var img1x = document.getElementById('screenshot-1x') as HTMLImageElement;

    img1x!.src = this.calculator.screenshot({
      height: 500,
      width: 500,
      targetPixelRatio: 2
    });

    console.log(img1x.src);

    //containerElt!.style.display = 'block';
    this.graphService.savePlottedImg(img1x.src).subscribe(
      responseData =>{
         // this.loading = false;
            //response
            let response = JSON.parse(JSON.stringify(responseData));
            console.log(response);
            if(response.image){
              console.log("success: "+response.image);
             // this.displayImg=response.image;
             // this.display=true;
             this.downloadFile(response.image);
            }
            else{
              alert("could not save graph");
            }
        }
    );
  }

  downloadFile(imageDownload:any) {
    var a = document.createElement('a');
    a.href = imageDownload;

    a.download = "output.png";
     document.body.appendChild(a);
     a.click();
     document.body.removeChild(a);
  }
  
  

  
}


    
    





