import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ConverterComponent} from './converter/converter.component'
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TemplateMatchingComponent } from './template-matching/template-matching.component';
import { UploadHistoryComponent } from './upload-history/upload-history.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { UnrecognizedImagesComponent } from './unrecognized-images/unrecognized-images.component';

import { LandingPageComponent } from './landing-page/landing-page.component';
import { WelcomePageComponent } from './welcome-page/welcome-page.component';


import { NavComponent } from './nav/nav.component';
import { LiveGraphing2Component } from './live-graphing2/live-graphing2.component';
import { TrackerComponent } from './tracker/tracker.component';


const routes: Routes = [
  /*{
    path: 'dashboard',
    component: DashboardComponent
  },*/
  {
    path: '',
    component: LoginComponent
  }/*,
  {
    path: 'upload',
    component: ConverterComponent,
    outlet:'navContent'
  }*/,
  {
    path: 'register',
    component: RegisterComponent
  }/*,
  {
    path: 'uploadHistory',
    component: UploadHistoryComponent
  }*/,
  {
    path: 'ForgotPassword',
    component: ForgotPasswordComponent
  }/*,
  {
    path: 'unrecognzied',
    component: UnrecognizedImagesComponent
  },
  {

    path: 'landing',
    component: LandingPageComponent
  },
  {
    path: 'welcome',
    component: WelcomePageComponent
  },
  {
    path: 'login',
    component: LoginComponent
  }


    path: 'nav',
    component: NavComponent
  },
  {
    path: 'livegraph',
    component: LiveGraphing2Component
  },
  {
    path: 'activitytracker',
    component: TrackerComponent
  }*/

  ,{
    path: 'nav',
    //canActivate: [AuthGuard],
    loadChildren: () =>
      import('./nav/nav-route/nav-route.module').then((m) => m.NavRouteModule),
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
declare global{
  interface Navigator{
     msSaveBlob:(blob: Blob,fileName:string) => boolean
     }
  }