import { Component, OnInit } from '@angular/core';
import {Title, Meta} from '@angular/platform-browser';
import { Router } from '@angular/router';

@Component({
  selector: 'app-welcome-page',
  templateUrl: './welcome-page.component.html',
  styleUrls: ['./welcome-page.component.scss']
})
export class WelcomePageComponent implements OnInit {

  constructor(private meta: Meta, private _router: Router) {
    meta.updateTag({name:'viewport', content:'width=device-width, initial-scale=1.0'});
   }

  ngOnInit(): void {
  }

  onSubmitUpload(){
    this._router.navigateByUrl("/dashboard")
  }

  onSubmitGraphing(){
    this._router.navigateByUrl("/dashboard")
  }

  onSubmitHistory(){
    this._router.navigateByUrl("/dashboard")
  }

  onSubmitUnrecognized(){
    this._router.navigateByUrl("/dashboard")
  }

  onSubmitTracker(){
    this._router.navigateByUrl("/dashboard")
  }

  onSubmitRetraining(){
    this._router.navigateByUrl("/dashboard")
  }

}
