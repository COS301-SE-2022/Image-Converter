import { Component, OnInit } from '@angular/core';
import {Title, Meta} from '@angular/platform-browser';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.scss']
})
export class LandingPageComponent implements OnInit {

  constructor(private meta: Meta) { 

    meta.updateTag({name:'viewport', content:'width=device-width, initial-scale=1.0'});
  }

  ngOnInit(): void {
  }

}
