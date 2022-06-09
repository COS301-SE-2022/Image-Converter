import { Component, OnInit } from '@angular/core';
import {MatDialogRef,MatDialog,MatDialogConfig} from '@angular/material/dialog';
import { ImagePopupComponent } from '../image-popup/image-popup.component';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-upload-history',
  templateUrl: './upload-history.component.html',
  styleUrls: ['./upload-history.component.scss']
})
export class UploadHistoryComponent implements OnInit {

  constructor(private dialog: MatDialog,private imgService: ConverterService) { }

  ngOnInit(): void {
    let respsonseBase64;
      this.imgService.getUploadHistory().subscribe(
        responseData =>{
          console.log("response");
           console.log("response here: "+responseData);
          respsonseBase64 = JSON.parse(JSON.stringify(responseData));
          console.log("response here: "+JSON.stringify(responseData));
        }
      );
  }

  uploadedImg: string[] = ['../../assets/purple.jpg', '../../assets/drag.png','../../assets/purple.jpg'];

  //code
  imageClick(image:any){

    console.log("click");
    //
    const configDialog = new MatDialogConfig();

    //send the processed version of the image (parameter)
    const dialogRef = this.dialog.open(ImagePopupComponent, {
      width: '40%',
      height: '80%',
      data: { img: image.image },
    });
  }
}
