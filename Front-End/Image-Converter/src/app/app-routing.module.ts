import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ConverterComponent} from './converter/converter.component'
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TemplateMatchingComponent } from './template-matching/template-matching.component';
import { UploadHistoryComponent } from './upload-history/upload-history.component';

const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  {
    path: '',
    component: LoginComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  {
    path: 'uploadHistory',
    component: UploadHistoryComponent
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