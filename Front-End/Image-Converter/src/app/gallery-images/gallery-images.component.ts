import { Component, OnInit } from '@angular/core';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';
import {ConverterService} from './../shared/converter.service';
import {MatDialogRef,MatDialog,MatDialogConfig} from '@angular/material/dialog';
import { ImagePopupComponent } from '../image-popup/image-popup.component';

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
  commentList: string[] = [];
  indexList: number[] = [];
  uuid:BigInteger[]=[];
  constructor(private dialog: MatDialog, private graphFolderData: ComponentCommunicationService,private imgService: ConverterService) { }

  ngOnInit(): void {
    this.subscription = this.graphFolderData.currentGraph.subscribe(selectedFolder => this.selectedFolder = selectedFolder);
    this.loading = true;
    this.imgService.GraphGallaryData(this.selectedFolder).subscribe(
      responseData =>{
        this.loading = false;
        let respsonseBase64 = JSON.parse(JSON.stringify(responseData));
        console.log("Gallery:", respsonseBase64);
      //  console.log("response here: "+JSON.stringify(responseData));
       
        for(let i=0;i<respsonseBase64.OriginalImage.length;i++){

            this.uploadedImgProcessed.push(respsonseBase64.proccesedImage[i]);
            this.commentList.push(respsonseBase64.Comments[i]);
            this.indexList.push(respsonseBase64.Index[i]);
            console.log("index: "+respsonseBase64.Index[i]);
           // this.uuid.push(respsonseBase64.Index[i]);
        }
      },//code below ensures that if token is invalid or expired user gets sent back to login
       (err) => {
        //if (err === 'Unauthorized') { this._router.navigateByUrl('/'); }
    });
  }

    //sends clicked image to popup
    imageClick(index:any){
      console.log("clicked");
      console.log('index', index);
      const configDialog = new MatDialogConfig();
      //send the processed version of the image (parameter)
      const dialogRef = this.dialog.open(ImagePopupComponent, {
        width: '40%',
        height: '80%',
        //Use the line of
        data: { img: '',imgProcessed:this.uploadedImgProcessed[index] , comment:this.commentList[index], index:this.indexList[index]},
      });
   
      //  dialogRef.afterClosed().subscribe((data) => {
      //    if (data != undefined) {
      //      //returned message
      //      console.log('returned message:'+data.request);
      //      this.loading = true;
      //      this.imgService.deleteImage(this.uuid[index]).subscribe(
      //        responseData =>{
      //              //response
                   
      //              this.uploadedImgProcessed=[];
      //              this.ngOnInit();
      //          }
      //      );
         
      //    } else {
      //      console.log('returned empty:');
      //    } //dialog closed
      //  });
   
    }

}
