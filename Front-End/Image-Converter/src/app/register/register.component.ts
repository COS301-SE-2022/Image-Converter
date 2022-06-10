import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Login } from '../classes/Login';
import { Register } from '../classes/Register';
import { CustomValidationService } from '../services/custom-validation.service';
import { ConverterService } from '../shared/converter.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  loginService: any;


  hide = true;
  _match!: boolean;
  buttonLogin = "";

  title = 'reactiveformproject';
  registerForm!: FormGroup; /*initialiting form type*/
  reactiveForm!: FormGroup;
  submitted = false;
  response!:{result:string,token:string};

  constructor(private registerService: ConverterService, private formBuilder: FormBuilder, private _router: Router) {}

  ngOnInit() { /*form validation*/
    this.registerForm = this.formBuilder.group({
      surname: ['', [Validators.required, Validators.minLength(2)]], /*minimum surname length*/
      name: ['', [Validators.required, Validators.minLength(2)]], /*minimum username length*/
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]], /*validation for password*/
      // cpassword: ['', [Validators.required, Validators.minLength(8)]],
      cpassword: new FormControl(null, [Validators.required, Validators.minLength(8)]) /*validation for confirmed password*/

    },
    {
      validators: this.MustMatch('password','cpassword') /*function for password validation, takes in password and 2nd entered password and compares the two*/
    })
  }

  
  login()
  {
    //intentionally left blank
  }
 
  // getters for user credentials
  get name() {  
    return this.registerForm.get('name');  
  } 
  get password() {  
    return this.registerForm.get('password');  
  } 
  get surname() {  
    return this.registerForm.get('surname');  
  } 
  get email() {  
    return this.registerForm.get('email');  
  } 
  get confirmPassword() {  
    return this.registerForm.get('cpassword');  
  } 


  MustMatch(controlName: string, matchingControl: string) /*function for password validation, takes in password and 2nd entered password and compares the two*/
  {
    return(formGroup: FormGroup)=>{
      const control = formGroup.controls[controlName];
      const matchingCont = formGroup.controls[matchingControl];
      if(matchingCont.errors && !matchingCont.errors.MustMatch)
      {
        return
      }

      if(control.value !== matchingCont.value)
      {
        matchingCont.setErrors({MustMatch:true}); //return true is passwords match
      }

      else{
        matchingCont.setErrors(null);
      }
    }
  }

  //submission of form
  onSubmit() {
    this.submitted = true;

    let authDetails:Register = {
      
      name: this.registerForm.get('name')!.value,
      surname: this.registerForm.get('surname')!.value,
      email: this.registerForm.get('email')!.value,
      password: this.registerForm.get('password')!.value,
      cpassword: this.registerForm.get('cpassword')!.value
    }

    this.registerService.register(authDetails).subscribe(
      responseData=>{
        console.log(responseData);
        this.response = JSON.parse(JSON.stringify(responseData));

        if(responseData.body.result == "success"){
          localStorage.setItem('token', responseData.body.token);
          this._router.navigateByUrl('/dashboard'); //navigate to dashboard on successful login
        }
      });
 
    // stop the process here if form is invalid
    if (this.registerForm.invalid) {
      return;
    }
 
    // alert('Registered successfully!');
  }
}

