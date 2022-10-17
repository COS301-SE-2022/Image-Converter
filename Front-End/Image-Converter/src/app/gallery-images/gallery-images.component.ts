import { Component, OnInit } from '@angular/core';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';
import {ConverterService} from './../shared/converter.service';
import {MatDialogRef,MatDialog,MatDialogConfig} from '@angular/material/dialog';
import { ImagePopupComponent } from '../image-popup/image-popup.component';
import { Validators } from '@angular/forms';

@Component({
  selector: 'app-gallery-images',
  templateUrl: './gallery-images.component.html',
  styleUrls: ['./gallery-images.component.scss']
})
export class GalleryImagesComponent implements OnInit {

  subscription!: Subscription;
  selectedFolder!: String;
  loading=false;
  dash: string = "-";
  

  //holds processed images
  uploadedImgProcessed: string[] = [];
  nameArr: string[] = ["line graph","test graph", "name3", "name4", "name5", "name6", "name7" ,"name8", "name9"];
  tagArr: string[] = ["16 Oct","random tag", "tag3", "tag4", "tag5", "tag6","tag7", "tag8", "tag9"];
  dateArr:string[] = [];

  
  
  uuid:BigInteger[]=[];
  constructor(private dialog: MatDialog, private graphFolderData: ComponentCommunicationService,private imgService: ConverterService) { }

  ngOnInit(): void {
    this.subscription = this.graphFolderData.currentGraph.subscribe(selectedFolder => this.selectedFolder = selectedFolder);
    this.loading = true;
    // console.log("in gallery top");
    this.imgService.GraphGallaryData(this.selectedFolder).subscribe(
      responseData =>{
        // console.log("in gallery");
        this.loading = false;
        let respsonseBase64 = JSON.parse(JSON.stringify(responseData));

      //  console.log("response here: "+JSON.stringify(responseData));
       
        for(let i=0;i<9;i++){ // respsonseBase64.OriginalImage.length
          
            this.uploadedImgProcessed.push(respsonseBase64.proccesedImage[i]);
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
       const configDialog = new MatDialogConfig();
   
       //send the processed version of the image (parameter)
       const dialogRef = this.dialog.open(ImagePopupComponent, {
         width: '40%',
         height: '80%',
         data: { img: '',imgProcessed:this.uploadedImgProcessed[index] },
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

     text: string='';
     check: string = this.text.replace(/[^a-zA-Z ]/g,"");

     textEntered(searchVal: string){
      this.text = searchVal.replaceAll(/[^a-zA-Z ]/g,' ');
      console.log(this.text);
     }

}
