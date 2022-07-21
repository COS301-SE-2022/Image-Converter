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
    code: new FormControl('', [Validators.required, Validators.minLength(4)])
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

  
  /*onSubmit() {
    
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
          this._router.navigateByUrl('/dashboard');
        }
      });
 
    // stop the process here if form is invalid
    if (this.registerForm.invalid) {
      return;
    }
 
    alert('Registered successfully!');
  }*/

  onSubmit(){
    document.getElementById("codeForm")!.style.display = "block";
    document.getElementById("reg")!.style.display = "none";
    console.log("in on sub")
    //once code is sent through and response is given
    //document.getElementById("resetForm")!.style.display="none";
   // document.getElementById("codeForm")!.style.display="inline-block";
   localStorage.setItem('name', this.registerForm.get('name')!.value);
   localStorage.setItem('surname',this.registerForm.get('surname')!.value);
   localStorage.setItem('email', this.registerForm.get('email')!.value);
   localStorage.setItem('pw', this.registerForm.get('password')!.value);

   let email = {
    email : this.registerForm.get('email')!.value
  } 

    this.registerService.registerEmailSend(email).subscribe(
      responseData =>{
            //response
            console.log(responseData);
            //this.response = JSON.parse(JSON.stringify(responseData));
    
            if(responseData.body.result == "success"){
              console.log("success");

            }
        }
    );
  }

  onSubmitCode()
  { 
    this.registerService.register(this.formCode.get('code')!.value).subscribe(
      responseData =>{
            //response
            if(responseData.body.result == "success"){
              console.log("success");
              localStorage.setItem('token', responseData.body.token);
              this._router.navigateByUrl('/dashboard');
            }
            else{
              alert("something went wrong");
            }
        }
    );
  }
}

