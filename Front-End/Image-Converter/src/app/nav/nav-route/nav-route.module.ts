import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NavRouteRoutingModule } from './nav-route-routing.module';

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
import { FilterComponent } from './../../filter/filter.component';
import { ToolbarComponent } from './../../toolbar/toolbar.component';
import { FooterComponent } from './../../footer/footer.component';
import { GalleryComponent } from './../../gallery/gallery.component';
import { GalleryImagesComponent } from './../../gallery-images/gallery-images.component';
import { SearchComponent } from './../../search/search.component';
import { SharedImagesComponent } from './../../shared-images/shared-images.component';
import { SharedImageComponent } from './../../shared-image/shared-image.component';

import { MaterialModule } from './../../material/material.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    ConverterComponent,
    DashboardComponent,
    TemplateMatchingComponent,
    UploadHistoryComponent,
    UnrecognizedImagesComponent,
    NavComponent,
    LiveGraphing2Component,
    TrackerComponent,
    SideBarComponent,
    ConversionComponent,
    ContactComponent,
    ImagePopupComponent,
    GraphPlottingComponent,
    AdminImagePopUpComponent,
    FilterComponent,
    ToolbarComponent,
    FooterComponent,
    GalleryComponent,
    GalleryImagesComponent,
    SearchComponent,
    SharedImagesComponent,
    SharedImageComponent
  ],
  imports: [
    CommonModule,
    NavRouteRoutingModule,
    MaterialModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ]
})
export class NavRouteModule { }
