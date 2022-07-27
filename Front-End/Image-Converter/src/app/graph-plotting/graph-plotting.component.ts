import { Component, OnInit } from '@angular/core';
import {FormGroup,FormControl,Validators} from '@angular/forms';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-graph-plotting',
  templateUrl: './graph-plotting.component.html',
  styleUrls: ['./graph-plotting.component.scss']
})
export class GraphPlottingComponent implements OnInit {

  constructor(private  graphPService: ConverterService,) { }

  ngOnInit(): void {
  }

  form = new FormGroup({  
    formula: new FormControl('', Validators.required)
  });

  get formula() {  
    return this.form.get('formula');  
  } 

  displayImg:any;
  //handle formula submission then displays drawn graph
  onFomulaSubmit()
  {
    let formula = {
      formula : this.form.get('formula')!.value
    } 
    let response:any=null;
    this.graphPService.postFormula(formula).subscribe(
      responseData =>{
            //response
            response = JSON.parse(JSON.stringify(responseData));
            console.log(response);
            if(response.image){
              console.log("success: "+response.image);
              this.displayImg=response.image;

             
            }
            else{
              alert("could not draw graph");
            }
        }
    );
  }
}
