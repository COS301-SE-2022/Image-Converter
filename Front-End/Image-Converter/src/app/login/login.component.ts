import { Component, OnInit } from '@angular/core';
import {FormGroup,FormControl,Validators} from '@angular/forms';
import {ConverterService} from './../shared/converter.service';
import { Observable, Subscriber } from 'rxjs';
import { Login } from '../classes/Login';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  hide = true;
  _match!: boolean;
  buttonLogin = "";

  constructor(private loginService: ConverterService) { }

  ngOnInit(): void {
  }

  form = new FormGroup({  
    username: new FormControl('', Validators.required),  
    password: new FormControl('', Validators.required),
    // submit: new FormControl()
  });

  get username() {  
    return this.form.get('username');  
  } 
  get password() {  
    return this.form.get('password');  
  } 

  register()
  {
    //intentionally left blank
  }
  onSubmit()
  {
    let authDetails:Login = {
      email : this.form.get('username')!.value,
      password : this.form.get('password')!.value
    } 

    this.loginService.login(authDetails).subscribe(
      responseData=>{
        console.log(responseData);
      });
      }
      
}
