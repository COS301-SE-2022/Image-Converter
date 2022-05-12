import { Injectable } from '@angular/core';
import { HttpClientModule, HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class ConverterService {

  constructor(private httpclient: HttpClient) { }

   // postImg sends request to back end to upload img
   postImg(img: File){
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
    const formData: FormData = new FormData();
    formData.append('Image', img, img.name);
    console.log("form: "+formData);
    return this.httpclient.post(
      'http://localhost:5000/api/User/uploadProfileImage',
      formData//,httpOptions
    );
  }
}
