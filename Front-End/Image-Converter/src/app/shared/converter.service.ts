import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClientModule, HttpClient, HttpHeaders } from '@angular/common/http';
import { Login } from '../classes/Login';
// import { stringify } from 'querystring';

@Injectable({
  providedIn: 'root'
})

export class ConverterService {

  constructor(private httpclient: HttpClient) { }

   // postImg sends request to back end to upload img
  
   //send request to back end to validate user login details
  login(formData: Login): Observable<any> {
    return this.httpclient.post(
      'http://localhost:5000/login',
      formData,{observe:'response'}
    );
  }
   postImg(data: string) {
     
     /* for future use
    var auth;
    if(localStorage.getItem('rememberMe')=="true"){
      auth=localStorage.getItem('token');
    }else{
      auth=sessionStorage.getItem('token');
    }

    
    const httpOptions = {
      headers: new HttpHeaders({
        Authorization: 'Bearer '+auth
      })
    };*/

    let pic = {picture: data};
    // console.log("form: "+data);
    return this.httpclient.post(
      'http://localhost:5000/picture',
      pic

    );
  }
  
}
