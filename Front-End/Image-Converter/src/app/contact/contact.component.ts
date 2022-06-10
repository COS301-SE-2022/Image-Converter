import { Message } from './../classes/Message';
import { Component, OnInit } from '@angular/core';
import {FormGroup,FormControl,Validators} from '@angular/forms';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent implements OnInit {

  constructor(private sendMessageService: ConverterService) { }

  ngOnInit(): void {

    this.form.patchValue({
      email: localStorage.getItem('email')
    });
    
  }
  
  //used for loadig spinner
  loading=false;

  form = new FormGroup({  
    email: new FormControl('', [Validators.required, Validators.email]),  
    message: new FormControl('', Validators.required),
  });

  onSubmit(){
      this.loading = true;

      let messageDetails:Message = {
        message : this.form.get('message')!.value
      } 

      this.sendMessageService.sendMessage(messageDetails).subscribe(
        responseData=>{
          this.loading = true;

          /*this.response = JSON.parse(JSON.stringify(responseData));
          // console.log(responseData.body.token);
          if(responseData.body.result == "success"){
            
          }*/
          //if success
          alert("Message successfully sent")
        });

  }
}
