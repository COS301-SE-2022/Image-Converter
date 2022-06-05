import { Component, OnInit } from '@angular/core';
import {MatDialogRef,MatDialog,MatDialogConfig} from '@angular/material/dialog';
import { ImagePopupComponent } from '../image-popup/image-popup.component';

@Component({
  selector: 'app-upload-history',
  templateUrl: './upload-history.component.html',
  styleUrls: ['./upload-history.component.scss']
})
export class UploadHistoryComponent implements OnInit {

  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {
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
