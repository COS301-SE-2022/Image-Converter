import { Component, OnInit } from '@angular/core';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-shared-images',
  templateUrl: './shared-images.component.html',
  styleUrls: ['./shared-images.component.scss']
})
export class SharedImagesComponent implements OnInit {

  uuid:BigInteger[]=[];
  //used for loadig spinner
  loading=false;
   //holds list of images
  images: string[] = [];

  constructor(private imgService: ConverterService) { }

  ngOnInit(): void {

    this.loading = true;
    let respsonse:any="";
      this.imgService.getListSharedImages("").subscribe(
        responseData =>{
          this.loading = false;
          respsonse = JSON.parse(JSON.stringify(responseData));
          for(let i=0;i<respsonse.OriginalImage.length;i++){

              this.images.push(respsonse.OriginalImage[i]);
              this.uuid.push(respsonse.Index[i]);
          }
        },
         (err) => {
         
      }
      );
  }

  imageClick(index:any)
  {

  }
}
