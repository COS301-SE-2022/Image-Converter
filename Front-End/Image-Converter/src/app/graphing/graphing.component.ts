import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { BarGraph } from '../classes/BarGraph';
import { ConverterService } from '../shared/converter.service';

@Component({
  selector: 'app-graphing',
  templateUrl: './graphing.component.html',
  styleUrls: ['./graphing.component.scss']
})
export class GraphingComponent implements OnInit {

  constructor(private barGraphService: ConverterService, private _router: Router) { }

  ngOnInit(): void {
  }


  response!:{result:string,token:string};
  form = new FormGroup({  
    label_1: new FormControl(''),  
    label_value_1: new FormControl(''),
  });



  get label_1() {  
    return this.form.get('label_1');  
  } 
  get label_value_1() {  
    return this.form.get('label_value_1');  
  } 

  onSubmit()
  {
    let authDetails:BarGraph = {
      label_1 : this.form.get('label_1')!.value,
      label_value_1 : this.form.get('label_value_1')!.value
    } 

    this.barGraphService.barGraph(authDetails).subscribe(
      responseData=>{
        console.log(responseData.body.result);
        this.response = JSON.parse(JSON.stringify(responseData));
 
      });
      }




}
