import { Component, OnInit } from '@angular/core';
import {Title, Meta} from '@angular/platform-browser';

@Component({
  selector: 'app-welcome-page',
  templateUrl: './welcome-page.component.html',
  styleUrls: ['./welcome-page.component.scss']
})
export class WelcomePageComponent implements OnInit {

  constructor(private meta: Meta) {
    meta.updateTag({name:'viewport', content:'width=device-width, initial-scale=1.0'});
   }

  ngOnInit(): void {
  }

}
