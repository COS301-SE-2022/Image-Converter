import { Component, OnInit } from '@angular/core';
import {FormGroup,FormControl,FormBuilder,Validators} from '@angular/forms';
import { Register } from '../classes/Register';
import { CustomValidationService } from '../services/custom-validation.service';
import { ConverterService } from '../shared/converter.service';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  // constructor(private registerService: ConverterService, private customValidator: CustomValidationService) { }

  // ngOnInit(): void {
  // }
  // form = new FormGroup({  
  //   name: new FormControl('', Validators.required),  
  //   surname: new FormControl('', Validators.required),  
  //   email: new FormControl('', Validators.required),  
  //   password: new FormControl('', Validators.required),
  //   confirmpassword: new FormControl('', Validators.required),
  //   // submit: new FormControl()
  // });

  // get name() {  
  //   return this.form.get('name');  
  // } 
  // get password() {  
  //   return this.form.get('password');  
  // } 
  // get confirmPassword() {  
  //   return this.form.get('confirmPassword');  
  // } 
  // get surname() {  
  //   return this.form.get('surname');  
  // } 
  // get email() {  
  //   return this.form.get('email');  
  // } 

  // register()
  // {
  //   //intentionally left blank
  // }
  // onSubmit()
  // {
  //   let authDetails:Register = {
  //     name: this.form.get('name')!.value,
  //     surname: this.form.get('surname')!.value,
  //     email: this.form.get('email')!.value,
  //     password: this.form.get('password')!.value,
  //     confirmPassword: this.form.get('confirmPassword')!.value,
  //   } 

  //   this.registerService.register(authDetails).subscribe(
  //     responseData=>{
  //       console.log(responseData);
  //     });
  //     }


  title = 'reactiveformproject';
  registerForm!: FormGroup;
  reactiveForm!: FormGroup;
  submitted = false;
 
  constructor(private registerService: ConverterService, private formBuilder: FormBuilder) {}
 
  ngOnInit() {
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
      });
 
    // stop the process here if form is invalid
    if (this.registerForm.invalid) {
      return;
    }
 
    alert('Registered successfully!');
  }
}
