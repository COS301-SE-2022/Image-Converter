/*
This file is used to group/contain all angular material modules imports that are used in the app
inorder to limit the amount of  angular material imports in the app.module.ts
*/
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import * as cardModule from '@angular/material/card';


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    cardModule.MatCardModule
  ],
  exports: [
    cardModule.MatCardModule
  ]
})
export class MaterialModule { }
