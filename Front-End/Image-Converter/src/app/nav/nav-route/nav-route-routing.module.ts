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
import { LandingPageComponent } from 'src/app/landing-page/landing-page.component';
// import { FooterComponent } from 'src/app/footer/footer.component';
import { GalleryComponent } from './../../gallery/gallery.component';
import { GalleryImagesComponent } from './../../gallery-images/gallery-images.component';
import { SearchComponent } from './../../search/search.component';

const routes: Routes = [
    {
        path: '',
        component: NavComponent,
        children: [
          {
            path: 'upload',
            component: ConverterComponent
          },
          {
            path: 'galleryimages',
            component: GalleryImagesComponent
          },
          {
            path: 'gallery',
            component: GalleryComponent
          },
          {
            path: 'uploadHistory',
            component: UploadHistoryComponent
          },
          {
            path: 'unrecognized',
            component: UnrecognizedImagesComponent
          },
          {
            path: 'livegraph',
            component: LiveGraphing2Component
          },
          {
            path: 'activitytracker',
            component: TrackerComponent
          }
          ,
          {
            path: 'landing',
            component: LandingPageComponent
          },
          {
            path: 'search',
            component: SearchComponent
          }
          
          // {
          //   path: 'footer',
          //   component: FooterComponent
          // }
          /*,
          { path: '', redirectTo: '/upload', pathMatch: 'full' },*/
        ],
    },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class NavRouteRoutingModule { }
