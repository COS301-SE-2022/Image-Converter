import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss']
})
export class ForgotPasswordComponent implements OnInit {

  constructor(private resetService: ConverterService) { }

  ngOnInit(): void {
  }

  _match!: boolean;
  buttonReset = "";

  form = new FormGroup({  
    email: new FormControl('', Validators.required)
  });

  formCode = new FormGroup({  
    code: new FormControl('', Validators.required)
  });

  onSubmit(){
    console.log("clicked");

    //once code is sent through and response is given
    //document.getElementById("resetForm")!.style.display="none";
   // document.getElementById("codeForm")!.style.display="inline-block";

   let email = {
    email : this.form.get('email')!.value
  } 

    this.resetService.ResetPassword(email).subscribe(
      responseData =>{
            //response
            console.log(responseData);
            //this.response = JSON.parse(JSON.stringify(responseData));
    
            if(responseData.body.result == "success"){
              //console.log("success");

              localStorage.setItem('codeEmail', this.form.get('email')!.value);
            }
        }
    );
  }

  onSubmitCode()
  {
    console.log("clicked code");
     this.resetService.resetPasswordCode(this.form.get('code')!.value).subscribe(
      responseData =>{
            //response
        }
    );
  }
}
