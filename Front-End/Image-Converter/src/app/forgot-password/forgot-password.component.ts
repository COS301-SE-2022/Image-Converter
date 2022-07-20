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

  constructor(private resetService: ConverterService, private _router: Router) { }

  ngOnInit(): void {
    document.getElementById("codeForm")!.style.display = "none";
    document.getElementById("passForm")!.style.display = "none";

  }
  // result!:{response:string};
  _match!: boolean;
  buttonReset = "";

  form = new FormGroup({  
    email: new FormControl('', Validators.required)
  });

  formCode = new FormGroup({  
    code: new FormControl('', Validators.required)
  });

  //new password form
  formPass = new FormGroup({  
    password: new FormControl('', Validators.required)
  });
  onSubmit(){
    console.log("clicked");

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
              alert("something went wrong");
            }
        }
    );
  }

  onSubmitCode()
  {

     this.resetService.resetPasswordCode(this.form.get('code')!.value).subscribe(
      responseData =>{
            //response
            
            if(responseData.body.result == "success"){
             
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
    this.resetService.resetPassword(this.formPass.get('password')!.value).subscribe(
      responseData =>{
            //response
            if(responseData.body.result == "success"){
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
