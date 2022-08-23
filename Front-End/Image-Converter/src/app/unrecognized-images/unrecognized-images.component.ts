import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { ImagePopupComponent } from '../image-popup/image-popup.component';
import { ConverterService } from '../shared/converter.service';

@Component({
  selector: 'app-unrecognized-images',
  templateUrl: './unrecognized-images.component.html',
  styleUrls: ['./unrecognized-images.component.scss']
})
export class UnrecognizedImagesComponent implements OnInit {

  constructor(private dialog: MatDialog,private imgService: ConverterService,private _router: Router) { }
    //holds unprocessed images
    uploadedImg: string[] = [];
    //holds unprocessed images
    uploadedImgProcessed: string[] = [];
  
    uuid:BigInteger[]=[];
    //used for loadig spinner
    loading=false;
  ngOnInit(): void {
    this.loading = true;
    let respsonseBase64:any="";
      this.imgService.getUnrecognizedGraphs().subscribe(
        responseData =>{
          this.loading = false;
           respsonseBase64 = JSON.parse(JSON.stringify(responseData));

         //console.log("response here: "+JSON.stringify(responseData));
         
          for(let i=0;i<respsonseBase64.OriginalImage.length;i++){

              this.uploadedImg.push(respsonseBase64.OriginalImage[i]);
              this.uploadedImgProcessed.push(respsonseBase64.proccesedImage[i]);
              console.log("index: "+respsonseBase64.Index[i]);
              this.uuid.push(respsonseBase64.Index[i]);
          }
        },//code below ensures that if token is invalid or expired user gets sent back to login
         (err) => {
          //if (err === 'Unauthorized') { this._router.navigateByUrl('/'); }
      }
      );
  }

  imageClick(index:any, arrayToUse:String){

    /* let image;
     if(arrayToUse=="uploaded"){
       image=this.uploadedImg[index];
     }
     else{
       image=this.uploadedImgProcessed[index];
     }*/
     
     const configDialog = new MatDialogConfig();
 
     //send the processed version of the image (parameter)
     const dialogRef = this.dialog.open(ImagePopupComponent, {
       width: '40%',
       height: '80%',
       data: { img: this.uploadedImg[index],imgProcessed:this.uploadedImgProcessed[index] },
     });
 
     dialogRef.afterClosed().subscribe((data) => {
       if (data != undefined) {
         //returned message
         console.log('returned message:'+data.request);
         this.loading = true;
         this.imgService.deleteImage(this.uuid[index]).subscribe(
           responseData =>{
                 //response
                 this.uploadedImg=[];
                 this.uploadedImgProcessed=[];
                 this.ngOnInit();
             }
         );
       
       } else {
         console.log('returned empty:');
       } //dialog closed
     });
 
   }


}
