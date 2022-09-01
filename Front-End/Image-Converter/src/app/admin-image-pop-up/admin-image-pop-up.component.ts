import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { UploadHistoryComponent } from '../upload-history/upload-history.component';

@Component({
  selector: 'app-admin-image-pop-up',
  templateUrl: './admin-image-pop-up.component.html',
  styleUrls: ['./admin-image-pop-up.component.scss']
})
export class AdminImagePopUpComponent implements OnInit {

  imageUrl!: string;
  graphType!:string;
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
  feedback(type:any)
  {
    this.dialogRef.close({request:"feedback",graphType:type});
  }

}
