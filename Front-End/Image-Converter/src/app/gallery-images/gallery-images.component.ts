import { Component, OnInit } from '@angular/core';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-gallery-images',
  templateUrl: './gallery-images.component.html',
  styleUrls: ['./gallery-images.component.scss']
})
export class GalleryImagesComponent implements OnInit {

  subscription!: Subscription;
  selectedFolder!: String;
  loading=false;

  //holds processed images
  uploadedImgProcessed: string[] = [];

  constructor(private graphFolderData: ComponentCommunicationService,private imgService: ConverterService) { }

  ngOnInit(): void {
    this.subscription = this.graphFolderData.currentGraph.subscribe(selectedFolder => this.selectedFolder = selectedFolder);
    this.loading = true;
    this.imgService.getUploadHistory().subscribe(
      responseData =>{
        this.loading = false;
        let respsonseBase64 = JSON.parse(JSON.stringify(responseData));

      //  console.log("response here: "+JSON.stringify(responseData));
       
        for(let i=0;i<respsonseBase64.OriginalImage.length;i++){

            this.uploadedImgProcessed.push(respsonseBase64.proccesedImage[i]);
            console.log("index: "+respsonseBase64.Index[i]);
           // this.uuid.push(respsonseBase64.Index[i]);
        }
      },//code below ensures that if token is invalid or expired user gets sent back to login
       (err) => {
        //if (err === 'Unauthorized') { this._router.navigateByUrl('/'); }
    });
  }

}
