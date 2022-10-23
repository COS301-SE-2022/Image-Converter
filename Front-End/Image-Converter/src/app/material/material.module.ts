
/*
This file is used to group/contain all angular material modules imports that are used in the app
inorder to limit the amount of  angular material imports in the app.module.ts
*/
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import * as cardModule from '@angular/material/card';
import { MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatInputModule } from '@angular/material/input';
import {MatListModule} from '@angular/material/list';
import {MatGridListModule} from '@angular/material/grid-list';
import { MatDialogModule } from '@angular/material/dialog';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatStepperModule} from '@angular/material/stepper';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    cardModule.MatCardModule,
    MatFormFieldModule,
    MatIconModule,
    MatButtonModule,
    MatInputModule,
    MatListModule,
    MatGridListModule,
    MatDialogModule,
    MatProgressSpinnerModule,
    MatSidenavModule,
    MatToolbarModule,
    MatStepperModule
  ],
  exports: [
    cardModule.MatCardModule,
    MatFormFieldModule,
    MatIconModule,
    MatButtonModule,
    MatInputModule,
    MatListModule,
    MatGridListModule,
    MatDialogModule,
    MatProgressSpinnerModule,
    MatSidenavModule,
    MatToolbarModule,
    MatStepperModule
  ]
})
export class MaterialModule { }
