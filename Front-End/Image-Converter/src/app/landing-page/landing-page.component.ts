import { Component, OnInit } from '@angular/core';
import {Title, Meta} from '@angular/platform-browser';
import { Router } from '@angular/router';
import { ViewportScroller } from '@angular/common';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.scss']
})
export class LandingPageComponent implements OnInit {

  constructor(private meta: Meta, private _router: Router, private scroller: ViewportScroller, private router: Router) { 

    meta.updateTag({name:'viewport', content:'width=device-width, initial-scale=1.0'});
  }

  ngOnInit(): void {
  }

  onSubmitCode(){
    this._router.navigateByUrl('/register');
    // alert("button working");
  }

  onSubmitLogin(){
    this._router.navigateByUrl('/login');
    // alert("button working");
  }

  scroll(el: HTMLElement) {
    el.scrollIntoView({behavior: 'smooth'});
}

goDown3() {
  this.router.navigate([], { fragment: "team" });
}

}
