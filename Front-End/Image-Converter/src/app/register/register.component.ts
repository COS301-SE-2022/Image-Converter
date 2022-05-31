import { Component, OnInit } from '@angular/core';
import {FormGroup,FormControl,Validators} from '@angular/forms';
import { Register } from '../classes/Register';
import { ConverterService } from '../shared/converter.service';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  constructor(private registerService: ConverterService) { }

  ngOnInit(): void {
  }
  form = new FormGroup({  
    name: new FormControl('', Validators.required),  
    surname: new FormControl('', Validators.required),  
    email: new FormControl('', Validators.required),  
    password: new FormControl('', Validators.required),
    // submit: new FormControl()
  });

  get name() {  
    return this.form.get('name');  
  } 
  get password() {  
    return this.form.get('password');  
  } 
  get surname() {  
    return this.form.get('surname');  
  } 
  get email() {  
    return this.form.get('email');  
  } 

  register()
  {
    //intentionally left blank
  }
  onSubmit()
  {
    let authDetails:Register = {
      
      name: this.form.get('name')!.value,
      surname: this.form.get('surname')!.value,
      email: this.form.get('email')!.value,
      password: this.form.get('password')!.value
      
    } 

    this.registerService.register(authDetails).subscribe(
      responseData=>{
        console.log(responseData);
      });
      }
}
