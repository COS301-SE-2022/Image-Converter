import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import {ConverterService} from './../shared/converter.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss']
})
export class ForgotPasswordComponent implements OnInit {
  

  constructor(private resetService: ConverterService, private _router: Router,private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    document.getElementById("codeForm")!.style.display = "none";
    document.getElementById("passForm")!.style.display = "none";
    this.formPass.controls['password'].setValue("");
  }
  // result!:{response:string};
  _match!: boolean;
  buttonReset = "";

  form = new FormGroup({  
    email: new FormControl('', [Validators.required, Validators.email])
  });

  formCode = new FormGroup({  
    code: new FormControl('', [Validators.pattern("^[0-9]*$"), Validators.minLength(4),Validators.maxLength(4)])
  });

  //new password form
  formPass = this.formBuilder.group({  
    password: new FormControl('', [Validators.required, Validators.minLength(8)]),
    cpassword: new FormControl('', [Validators.required, Validators.minLength(8)])
  },
  {
      validators: this.MustMatch('password','cpassword')
    });

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
  onSubmit()
  {
    //once code is sent through and response is given
 
    let email = {
      email : this.form.get('email')!.value
      } 
  let response;
    this.resetService.ResetPassword(email).subscribe(
      responseData =>{
            //response
            response = JSON.parse(JSON.stringify(responseData));
            console.log(response.body.response)
            if(response.body.response == "success"){
              //console.log("success");

              localStorage.setItem('codeEmail', this.form.get('email')!.value);
              document.getElementById("resetForm")!.style.display="none";
              document.getElementById("codeForm")!.style.display="block";
          
            }
            else{
              alert("User Does not exist");
            }
        }
    );
  }

  onSubmitCode()
  {  
     this.resetService.resetPasswordCode(this.formCode.get('code')!.value).subscribe(
      responseData =>{
            //response
            let response = JSON.parse(JSON.stringify(responseData));
            console.log(response.body.response)
            if(response.body.response == "success"){
             
              document.getElementById("codeForm")!.style.display = "none";
              document.getElementById("passForm")!.style.display = "block";
            }
            else{
              alert("something went wrong");
            }
        }
    );
  }

  //sends new password to the backend
  submitPass()
  {
    let response;
    this.resetService.resetPassword(this.formPass.get('password')!.value).subscribe(
      responseData =>{
            //response
            response = JSON.parse(JSON.stringify(responseData));
            if(response.body.response == "success"){
              alert("password successfully reset");
              this._router.navigateByUrl('/');//can be changed to redirect to dashboard if token is returned
            }
            else{
              alert("something went wrong");
            }
        }
    );
  }
}
