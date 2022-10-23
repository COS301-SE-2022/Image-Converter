import { Component, OnInit } from '@angular/core';
import {MatDialogRef,MatDialog,MatDialogConfig} from '@angular/material/dialog';
import { ImagePopupComponent } from '../image-popup/image-popup.component';
import {ConverterService} from './../shared/converter.service';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-share-page',
  templateUrl: './share-page.component.html',
  styleUrls: ['./share-page.component.scss']
})
export class SharePageComponent implements OnInit {

  loading=false;

  uploadedImgProcessed: string[] = [];
  commentList: string[] = [];
  indexList: number[] = [];

  nameArr: string[] = [];
  tagArr: string[] = [];
  dateArr:string[] = [];

  constructor(private dialog: MatDialog, private graphFolderData: ComponentCommunicationService,private imgService: ConverterService) { }

  ngOnInit(): void {
  }

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
  
    
  }

}
