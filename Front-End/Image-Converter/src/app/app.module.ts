import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ConverterComponent } from './converter/converter.component';
import { MaterialModule } from './material/material.module';
import {ConverterService} from './shared/converter.service';
import { FilterComponent } from './filter/filter.component';
import { ComponentCommunicationService } from './shared/component-communication.service';
import { LoginComponent } from './login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RegisterComponent } from './register/register.component';
import { SideBarComponent } from './side-bar/side-bar.component';
import { ConversionComponent } from './conversion/conversion.component';
import { UploadHistoryComponent } from './upload-history/upload-history.component';
import { ContactComponent } from './contact/contact.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TemplateMatchingComponent } from './template-matching/template-matching.component';
import { ImagePopupComponent } from './image-popup/image-popup.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { GraphPlottingComponent } from './graph-plotting/graph-plotting.component';
import { Router, RouterModule} from '@angular/router';

@NgModule({
  declarations: [
    AppComponent,
    ConverterComponent,
    FilterComponent,
    LoginComponent,
    RegisterComponent,
    SideBarComponent,
    ConversionComponent,
    UploadHistoryComponent,
    ContactComponent,
    DashboardComponent,
    TemplateMatchingComponent,
    ImagePopupComponent,
    ForgotPasswordComponent,
    GraphPlottingComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule
  ],
  providers: [ConverterService,ComponentCommunicationService, Router],
  bootstrap: [AppComponent]
})
export class AppModule { }
