import { Injectable } from '@angular/core';
import { HttpClientModule, HttpClient, HttpHeaders } from '@angular/common/http';
// import { stringify } from 'querystring';

@Injectable({
  providedIn: 'root'
})

export class ConverterService {

  constructor(private httpclient: HttpClient) { }

   // postImg sends request to back end to upload img

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
