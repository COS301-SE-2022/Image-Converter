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
     //if user was redirected from shared image
      if(localStorage.getItem('imageParam') && localStorage.getItem('imageParam')!="")
      {
        this._router.navigateByUrl('/nav/sharedmage?image='+localStorage.getItem('imageParam'));
      }
  }

  onSubmitUpload(){
    this._router.navigateByUrl('/nav/upload');
  }

  onSubmitGraphing(){
    this._router.navigateByUrl('/nav/livegraph');
  }

  onSubmitHistory(){
    this._router.navigateByUrl('/nav/uploadHistory');
  }

  onSubmitUnrecognized(){
    this._router.navigateByUrl('/nav/unrecognized');
  }

  onSubmitTracker(){
    this._router.navigateByUrl('/nav/activitytracker');
  }

  onSubmitRetraining(){
    this._router.navigateByUrl('/nav/upload');
  }

  onSubmitGallery(){
    this._router.navigateByUrl('/nav/gallery');
  }

}
