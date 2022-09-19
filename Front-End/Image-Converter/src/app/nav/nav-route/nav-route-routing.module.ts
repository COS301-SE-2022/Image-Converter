import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ConverterComponent} from './../../converter/converter.component';
import { DashboardComponent } from './../../dashboard/dashboard.component';
import { TemplateMatchingComponent } from './../../template-matching/template-matching.component';
import { UploadHistoryComponent } from './../../upload-history/upload-history.component';
import { UnrecognizedImagesComponent } from './../../unrecognized-images/unrecognized-images.component';
import { NavComponent } from './../../nav/nav.component';
import { LiveGraphing2Component } from './../../live-graphing2/live-graphing2.component';
import { TrackerComponent } from './../../tracker/tracker.component';
import { SideBarComponent } from './../../side-bar/side-bar.component';
import { ConversionComponent } from './../../conversion/conversion.component';
import { ContactComponent } from './../../contact/contact.component';
import { ImagePopupComponent } from './../../image-popup/image-popup.component';
import { GraphPlottingComponent } from './../../graph-plotting/graph-plotting.component';
import { AdminImagePopUpComponent } from './../../admin-image-pop-up/admin-image-pop-up.component';

const routes: Routes = [
    {
        path: '',
        component: NavComponent,
        children: [
        {
            path: 'dashboard',
            component: DashboardComponent
          },
          {
            path: 'upload',
            component: ConverterComponent
          },
          {
            path: 'uploadHistory',
            component: UploadHistoryComponent
          },
          {
            path: 'unrecognzied',
            component: UnrecognizedImagesComponent
          }/*,
          {
            path: 'nav',
            component: NavComponent
          }*/,
          {
            path: 'livegraph',
            component: LiveGraphing2Component
          },
          {
            path: 'activitytracker',
            component: TrackerComponent
          }/*,
          { path: '', redirectTo: '/upload', pathMatch: 'full' },*/
        ],
    },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class NavRouteRoutingModule { }
