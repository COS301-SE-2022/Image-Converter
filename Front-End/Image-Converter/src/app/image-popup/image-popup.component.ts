import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef,MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-image-popup',
  templateUrl: './image-popup.component.html',
  styleUrls: ['./image-popup.component.scss']
})
export class ImagePopupComponent implements OnInit {

  //holds the url of the image passed into this component
  imageUrl!: string;

  constructor(@Inject(MAT_DIALOG_DATA) public data: {img: string}) { }

  ngOnInit(): void {
    this.imageUrl=this.data.img;
    console.log(this.imageUrl);
  }
 
  downloadFile() {
    var a = document.createElement('a');
    a.href = this.imageUrl;
    var imgBckend = a.href;
    a.download = "output.png";
     document.body.appendChild(a);
     a.click();
     document.body.removeChild(a);
  }
}
