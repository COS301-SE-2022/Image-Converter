import { Component, OnInit } from '@angular/core';
// // import {Desmos} from 'desmos';
import html2canvas from 'html2canvas';

// declare var Desmos: any;

@Component({
  selector: 'app-live-graphing2',
  templateUrl: './live-graphing2.component.html',
  styleUrls: ['./live-graphing2.component.scss']
})
export class LiveGraphing2Component implements OnInit {
  myScriptElement: HTMLScriptElement;
  Desmos: any;

  constructor() { 
    this.myScriptElement = document.createElement("script");
    this.myScriptElement.src = "https://www.desmos.com/api/v1.7/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6";
    document.body.appendChild(this.myScriptElement);
  }

  ngOnInit(): void {

      this.myScriptElement.onload = () => {
        this.Desmos = (<any>window).Desmos;
        console.log('loaded');
        document.getElementsByTagName('head')[0].appendChild(this.myScriptElement);
        var elt = document.getElementById('calculator');
        // var calculator = this.Desmos.GraphingCalculator(elt, { keypad: true, expressions: true, settingsMenu: false, expressionsCollapsed: true });
        var calculator = this.Desmos.GraphingCalculator(elt);

      
        calculator.setExpression({});
        // calculator.setExpression({id: 'graph1', latex: 'y=x^2'});

        // var img1x = document.getElementById('screenshot-1x');
        var fullsize = calculator.screenshot();

        var img = document.createElement('img');

        img.src = fullsize;

        document.body.appendChild(img);
        
    }

  

  }

    getName()
    {
      alert("yessir")
    }
    // captureScreenshots () {
    // img1x.src = calculator.screenshot({
    //   height: 500,
    //   width: 500
    // });




}
