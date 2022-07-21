import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClientModule, HttpClient, HttpHeaders } from '@angular/common/http';
import { Login } from '../classes/Login';
import { Register } from '../classes/Register';
import { Message } from '../classes/Message';
// import { stringify } from 'querystring';

@Injectable({
  providedIn: 'root'
})

export class ConverterService {

  constructor(private httpclient: HttpClient) { }

   // postImg sends request to back end to upload img
  
   //send request to back end to validate user login details
  login(formData: Login): Observable<any> {
    console.log(formData);
    return this.httpclient.post(
      'http://localhost:5000/login',
      formData,{observe:'response'}
    );
  }
  
  register(codePar:any) : Observable<any> {

    let data = {name: localStorage.getItem('name'),
                surname: localStorage.getItem('surname'),
                email: localStorage.getItem('email'),
                pw: localStorage.getItem('pw'),
                code: codePar
                };

    return this.httpclient.post(
      'http://localhost:5000/register',
      data,{observe:'response'}
    );
  }
   postImg(data: string) {
     
    // var auth=sessionStorage.getItem('token');
    var tok = localStorage.getItem('token');
    console.log(tok);
    let headers: HttpHeaders = new HttpHeaders({'x-access-token': tok!});
    const httpOptions:Object = {
      headers: headers
    };
    console.log(httpOptions);
    let pic = {picture: data};
    // console.log("form: "+data);
    return this.httpclient.post(
      'http://localhost:5000/picture',
      pic,httpOptions
    );
  }

  //fetches users image upload history
  getUploadHistory(){

    let token = localStorage.getItem('token');
    
    let headers: HttpHeaders = new HttpHeaders({'x-access-token': token!});
    const httpOptions:Object = {
      headers: headers
    };
    let data = {data: ''};
    return this.httpclient.get(
      'http://localhost:5000/uploadhistory',
      httpOptions
    );
  }

  //sends request to delete images
  deleteImage(id:any){

    var tok = localStorage.getItem('token');
  
    let headers: HttpHeaders = new HttpHeaders({'x-access-token': tok!});
    const httpOptions:Object = {
      headers: headers
    };
    
    let pic = {index: id};

    return this.httpclient.post(
      'http://localhost:5000/deletehistory',
      pic,httpOptions
    );
  }

  //sends users message
  sendMessage(messageDetails:Message){

    var token = localStorage.getItem('token');
  
    let headers: HttpHeaders = new HttpHeaders({'x-access-token': token!});
    const httpOptions:Object = {
      headers: headers
    };
    return this.httpclient.post(
      'http://localhost:5000/feedback',
      messageDetails,httpOptions
    );
  }

  //sends users email to where reset code will be sent
  ResetPassword(email:any): Observable<any>
  { 
    console.log(JSON.stringify(email));
    let request = {email: email}
    return this.httpclient.post(
      'http://localhost:5000/resetpasswordemail',
      email,{observe:'response'}
    );
  }

  resetPasswordCode(code:any): Observable<any>
  { 
    let request = {email: localStorage.getItem('codeEmail'),
                  code:code}
    return this.httpclient.post(
      'http://localhost:5000/resetpasswordcode',
      request,{observe:'response'}
    );
  }

  //sends new password to server
  resetPassword(pass:any): Observable<any>
  {
    let request = {email: localStorage.getItem('codeEmail'),
                    newPassword:pass}
    return this.httpclient.post(
      'http://localhost:5000/resetpassword',
      request,{observe:'response'}
    );
  }

  //sends users email to where code will be sent
  registerEmailSend(email:any): Observable<any>
  { 
    return this.httpclient.post(
      'http://localhost:5000/sendEmail',
      email,{observe:'response'}
    );
  }

  
}
