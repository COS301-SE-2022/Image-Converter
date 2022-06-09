import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef,MAT_DIALOG_DATA } from '@angular/material/dialog';
import { UploadHistoryComponent } from '../upload-history/upload-history.component';

@Component({
  selector: 'app-image-popup',
  templateUrl: './image-popup.component.html',
  styleUrls: ['./image-popup.component.scss']
})
export class ImagePopupComponent implements OnInit {

  //holds the url of the image passed into this component
  imageUrl!: string;
  imageProcessedUrl!: string;
  constructor(@Inject(MAT_DIALOG_DATA) public data: {img: string,imgProcessed:string},public dialogRef: MatDialogRef<UploadHistoryComponent>) { }
  
  ngOnInit(): void {
    this.imageUrl=this.data.img;
    this.imageProcessedUrl=this.data.imgProcessed;
    console.log(this.imageUrl);
  }
 
  downloadFile(imageDownload:any) {
    var a = document.createElement('a');
    a.href = imageDownload;

    a.download = "output.png";
     document.body.appendChild(a);
     a.click();
     document.body.removeChild(a);
  }

  deleteImages()
  {
    this.dialogRef.close({request:"delete"});
  }
}
