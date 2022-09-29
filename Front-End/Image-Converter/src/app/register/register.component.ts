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
  buttonReset = "";
  
  title = 'reactiveformproject';
  registerForm!: FormGroup;
  reactiveForm!: FormGroup;
  submitted = false;
  response!:{result:string,token:string};
  loading=false;

  constructor(private registerService: ConverterService, private formBuilder: FormBuilder, private _router: Router) {}

  ngOnInit() {

    document.getElementById("codeForm")!.style.display = "none";

    this.registerForm = this.formBuilder.group({
      surname: ['', [Validators.required, Validators.minLength(2)]],
      name: ['', [Validators.required, Validators.minLength(2)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
      // cpassword: ['', [Validators.required, Validators.minLength(8)]],
      cpassword: new FormControl(null, [Validators.required, Validators.minLength(8)])

    },
    {
      validators: this.MustMatch('password','cpassword')
    })
  }
  formCode = new FormGroup({  
    code: new FormControl('', [Validators.required,Validators.pattern("^[0-9]*$"), Validators.minLength(4),Validators.maxLength(4)])
  });
  // form = new FormGroup({  
  //   username: new FormControl('', Validators.required),  
  //   password: new FormControl('', Validators.required),
  //   // submit: new FormControl()
  // });

  login()
  {
    //intentionally left blank
  }
 
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


  MustMatch(controlName: string, matchingControl: string)
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
        matchingCont.setErrors({MustMatch:true});
      }

      else{
        matchingCont.setErrors(null);
      }
    }
  }

  //sends registration user details the backend
  onSubmit(){
    this.loading=true;
    //once code is sent through and response is given
    //document.getElementById("resetForm")!.style.display="none";
   // document.getElementById("codeForm")!.style.display="inline-block";
   localStorage.setItem('name', this.registerForm.get('name')!.value);
   localStorage.setItem('surname',this.registerForm.get('surname')!.value);
   localStorage.setItem('email', this.registerForm.get('email')!.value);
   localStorage.setItem('password', this.registerForm.get('password')!.value);

   let email = {
    email : this.registerForm.get('email')!.value
  } 
    let response;
    this.registerService.registerEmailSend(email).subscribe(
      responseData =>{
            //response
            this.loading=false;
            console.log(responseData);
            //this.response = JSON.parse(JSON.stringify(responseData));
            response = JSON.parse(JSON.stringify(responseData));
            if(response.body.response == "success"){
              console.log("success");
              document.getElementById("codeForm")!.style.display = "block";
              document.getElementById("reg")!.style.display = "none";
            }
        }
    );
  }
  //sends verification code to the backend
  onSubmitCode()
  { this.loading=true;
    let response;
    this.registerService.register(this.formCode.get('code')!.value).subscribe(
      responseData =>{
            //response
            this.loading=false;
            response = JSON.parse(JSON.stringify(responseData));
            console.log(response.body.result);
            if(response.body.result == "success"){
              console.log("success");
              localStorage.setItem('token', responseData.body.token);
              this._router.navigateByUrl('/welcome');
            }
            // else{
            //   alert("something went wrong");
            // }
        }
    );
  }

  onSubmitLogin()
  {
    this._router.navigateByUrl('/login');
  }
}

