import { Injectable } from '@angular/core';
import { HttpClientModule, HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class ConverterService {

  constructor(private httpclient: HttpClient) { }

   // postImg sends request to back end to upload img
   postImg(img: File){

    //convert to base64
    /*var reader = new FileReader();
    reader.readAsDataURL(img);
    reader.onload = function () {
      console.log(reader.result);
      var pic = {
        picture: reader.result
      };
    };
    reader.onerror = function (error) {
      console.log('Error: ', error);
    };*/
 
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
    // Create the Project:
    var pic = {
      picture: "jjjjjjjjjjjggggggggggggggggggggghhh"
    };

    //const formData: FormData = new FormData();
    //formData.append('Image', img, img.name);
    //console.log("form: "+formData);
    return this.httpclient.post(
      'http://127.0.0.1:5000/picture',
      pic,{observe:'response'}
    );
  }
  
}
