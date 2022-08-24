import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  constructor(private _router: Router,private sendMessageService: ConverterService) { }

  ngOnInit(): void {
    if(!localStorage.getItem('token') && localStorage.getItem('token')=="")
    {
      this._router.navigateByUrl('/');
    }
    //check if admin
    this.sendMessageService.userType().subscribe(
      responseData=>{
       
       let response = JSON.parse(JSON.stringify(responseData));
        
         console.log(response);
        if(response.response == "success"){
            if(response.userType)
            {
              document.getElementById("contact")!.style.display = "none";
              document.getElementById("cont")!.style.display = "none";
            }
            else{
              
              document.getElementById("unrecognizedImg")!.style.display = "none";
              document.getElementById("unrec")!.style.display = "none";
            }
        }
        else{//hide admin content by default
          document.getElementById("unrecognizedImg")!.style.display = "none";
          document.getElementById("unrec")!.style.display = "none";
        }
       
      });
  }

  toHome() {
    var x = document.getElementById("home") as HTMLLinkElement
    x.scrollIntoView();
  }
  toImageUpload(){
    var x = document.getElementById("imageUpload") as HTMLLinkElement
    x.scrollIntoView();
  }
  // toImageFilter(){
  //   var x = document.getElementById("imageFilter") as HTMLLinkElement
  //   x.scrollIntoView();
  // }
  toConversionFormat(){
    var x = document.getElementById("conversionFormat") as HTMLLinkElement
    x.scrollIntoView();
  }
  toUploadHistory(){
    var x = document.getElementById("uploadHistory") as HTMLLinkElement
    x.scrollIntoView();
  }
  toContact(){
    var x = document.getElementById("contact") as HTMLLinkElement
    x.scrollIntoView();
  }
  toGraphing(){
    var x = document.getElementById("graphPlotting") as HTMLLinkElement
    x.scrollIntoView();
  }
  

  logout()
  {
    localStorage.setItem('token', "");
    this._router.navigateByUrl('/');
  }

  toUnrecognized() {
    var x = document.getElementById("unrecognizedImg") as HTMLLinkElement
    x.scrollIntoView();
  }
}


