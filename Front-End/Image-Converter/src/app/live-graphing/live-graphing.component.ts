import { ScriptService } from './../services/script.service';
import { Component, OnInit } from '@angular/core';
//import Desmos from 'desmos';

@Component({
  selector: 'app-live-graphing',
  templateUrl: './live-graphing.component.html',
  styleUrls: ['./live-graphing.component.scss']
})
export class LiveGraphingComponent implements OnInit {

  constructor(private scriptService: ScriptService) { }


  ngOnInit(): void {
    this.scriptService.load('desmos').then(data => {
      console.log('script loaded ', data);
    let calcElt = document.getElementById('calculator');
    this.calculator = data[0].GraphingCalculator(calcElt!);
    this.calculator.setExpression({latex: 'x^2+y^2=10'});
  }).catch(error => console.log(error));
  }
   calculator!:any;
    /*calcElt = document.getElementById('calculator');
    calculator = Desmos.GraphingCalculator(calcElt);
    calculator.setExpression({latex: 'x^2+y^2=10'});*/

   /* btnElt = document.getElementById('screenshot-button');
    btnElt.addEventListener('click', captureScreenshots);

    containerElt = document.getElementById('screenshot-container');
    img1x = document.getElementById('screenshot-1x');
    

    captureScreenshots () {
      this.img1x!.src = calculator.screenshot({
        height: 400,
        width: 400
      });
      containerElt.style.display = 'block';
        }*/
    }
