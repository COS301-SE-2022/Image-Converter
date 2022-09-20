import { Component, OnInit } from '@angular/core';
import {FormGroup,FormControl,Validators} from '@angular/forms';
import {ConverterService} from './../shared/converter.service';
import { Observable, Subscriber } from 'rxjs';
import { Login } from '../classes/Login';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  hide = true;
  _match!: boolean;
  buttonLogin = "";
  loading=false;
  constructor(private loginService: ConverterService, private _router: Router) { }

  ngOnInit(): void {
  }
  response!:{result:string,token:string};
  form = new FormGroup({  
    username: new FormControl('', [Validators.required, Validators.email]),  
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
    this.loading=true;
    let authDetails:Login = {
      email : this.form.get('username')!.value,
      password : this.form.get('password')!.value
    } 

    this.loginService.login(authDetails).subscribe(
      responseData=>{
        this.loading=false;
        console.log(responseData.body.response);
        this.response = JSON.parse(JSON.stringify(responseData));
        // console.log(responseData.body.token);
        if(responseData.body.response == "success"){
          localStorage.setItem('token', responseData.body.token);
          localStorage.setItem('email', this.form.get('username')!.value);
          this._router.navigateByUrl('/welcome');
        }
        // this._router.navigateByUrl('/dashboard');
      });
      }
      
}
