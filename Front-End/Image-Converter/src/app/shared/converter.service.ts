import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClientModule, HttpClient, HttpHeaders } from '@angular/common/http';
import { Login } from '../classes/Login';
import { Register } from '../classes/Register';
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
  
  register(formData: Register) : Observable<any> {
    return this.httpclient.post(
      'http://localhost:5000/register',
      formData,{observe:'response'}
    );
  }
   postImg(data: string) {
     
    var auth=sessionStorage.getItem('token');
    
    const httpOptions:Object = {
      headers: new HttpHeaders({
        Authorization:auth!
      })
    };
    let pic = {picture: data};
    // console.log("form: "+data);
    return this.httpclient.post(
      'http://localhost:5000/picture',
      pic,httpOptions
    );
  }
  
}
