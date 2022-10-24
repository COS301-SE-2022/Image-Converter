import {Component, OnInit} from '@angular/core';
import {ComponentCommunicationService} from '../shared/component-communication.service';
import {Subscription} from 'rxjs';
import {COMMA, ENTER} from '@angular/cdk/keycodes';
import {MatChipInputEvent} from '@angular/material/chips';
import {ConverterService} from './../shared/converter.service';
import {MatDialogRef, MatDialog, MatDialogConfig} from '@angular/material/dialog';
import {ImagePopupComponent} from '../image-popup/image-popup.component';
import {Validators} from '@angular/forms';
import {Message} from "../classes/Message";
import {MatDialogRef,MatDialog,MatDialogConfig} from '@angular/material/dialog';
import { ImagePopupComponent } from '../image-popup/image-popup.component';
import { Validators } from '@angular/forms';
import { Router } from '@angular/router';

export interface Tag {
  name: string;
}

export interface TagList {
  pos: number;
  name: any[];
  imgName: string;
  check
    : string;
  tags: any[];
}

@Component({
  selector: 'app-gallery-images',
  templateUrl: './gallery-images.component.html',
  styleUrls: ['./gallery-images.component.scss']
})
export class GalleryImagesComponent implements OnInit {

  subscription!: Subscription;
  selectedFolder!: string;
  loading = false;
  dash: string = "-";


  //holds processed images
  uploadedImgProcessed: string[] = [];
  commentList: string[] = [];
  indexList: number[] = [];
  temp: TagList[] = [];
  tempData: string = "";

  // ["line graph","test graph", "name3", "name4", "name5", "name6", "name7" ,"name8", "name9"];
  // ["16 Oct","random tag", "tag3", "tag4", "tag5", "tag6","tag7", "tag8", "tag9"];
  nameArr: string[] = [];
  tagArr: string[] = [];
  dateArr: string[] = [];
  tags: string[] = [];



  textT1: any[] = [];
  uuid:any[]=[];
  constructor(private _router: Router,private dialog: MatDialog, private graphFolderData: ComponentCommunicationService,private imgService: ConverterService) { }

  ngOnInit(): void {

    this.subscription = this.graphFolderData.currentGraph.subscribe(selectedFolder => this.selectedFolder = selectedFolder);
    this.loading = true;

    //when not category has been selected
    if(this.selectedFolder=='none')
    {
      this._router.navigateByUrl('/nav/gallery');
    }

    if(this.selectedFolder == "Line graphs")
      this.selectedFolder = "line graph";
    else if (this.selectedFolder == "Bar graphs")
      this.selectedFolder = "bar graph";
    else if (this.selectedFolder == "Pie charts")
      this.selectedFolder = "pie chart";
    else if (this.selectedFolder == "Tables")
      this.selectedFolder = "table";
    else if (this.selectedFolder == "Flow charts")
      this.selectedFolder = "flow chart";

    this.imgService.GraphGallaryData(this.selectedFolder).subscribe(
      responseData => {
        this.loading = false;
        let respsonseBase64 = JSON.parse(JSON.stringify(responseData));
        console.log("Gallery:", respsonseBase64);

        for (let i = 0; i < respsonseBase64.OriginalImage.length; i++) { // respsonseBase64.OriginalImage.length
          if (i == respsonseBase64.Tags.length)
            break;
          this.uploadedImgProcessed.push(respsonseBase64.proccesedImage[i]);
          this.commentList.push(respsonseBase64.Comments[i]);
          this.indexList.push(respsonseBase64.Index[i]);
          this.tagArr.push(respsonseBase64.Tags[i]);
          this.nameArr.push(respsonseBase64.Names[i]);
          this.uuid.push(respsonseBase64.Guids[i]);
          console.log("index: " + respsonseBase64.Tags[i]);

          // this.uuid.push(respsonseBase64.Index[i]);
        }
        let textT: string[] = [];

        let data: string;
        for (let index = 0; index < this.tagArr.length; index++) {
          let words = this.tagArr[index];
          this.tempData = this.tagArr[index];
          data = "";
          for (let j = 0; j < words.length; j++) {
            if (words[j] == '{' || words[j] == '}' || words[j] == '' || words[j] == ' ')
              continue;
            else if (words[j] != ',') {
              data += words[j];
              if (j == words.length - 1) {
                textT.push(data);
                this.textT1.push(data);
              }
            } else if (words[j] == ',') {
              textT.push(data);
              this.textT1.push(data);
              data = '';
            }
          }
          // console.log("Che",textT);
          this.temp.push({pos: index, name: textT, imgName: this.nameArr[index], check: this.tempData, tags: [1, 2, 3, 4]});
          console.log("temp", this.temp);
          textT = [];
          // textT.push(data);
        }
      },//code below ensures that if token is invalid or expired user gets sent back to login
      (err) => {
        //if (err === 'Unauthorized') { this._router.navigateByUrl('/'); }
      });
  }

  //sends clicked image to popup
  imageClick(index: any) {
    console.log("clicked");
    console.log('index', index);
    const configDialog = new MatDialogConfig();
    //send the processed version of the image (parameter)
    const dialogRef = this.dialog.open(ImagePopupComponent, {
      width: '40%',
      height: '80%',
      //Use the line of
      data: { img: '',imgProcessed:this.uploadedImgProcessed[index] , comment:this.commentList[index], index:this.indexList[index],uuid:this.uuid[index]},
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

  text: string = '';
  check: string = this.text.replace(/[^a-zA-Z ]/g, "");
  flags: boolean[] = [];
  flag: boolean = true;
  check1: boolean = false;

  textEntered(searchVal: string) {


    this.text = searchVal.replaceAll(/[^\w\s.]/gi, ' ');
  }


  //Image tags
  addOnBlur = true;
  readonly separatorKeysCodes = [ENTER, COMMA] as const;


  add(event: MatChipInputEvent, position: number): void {
    console.log("TagNum", position)
    const value = (event.value || '').trim();

    if (value) {
      for (const element of this.temp) {
        if (element.pos == position) {
          let data = value;
          if (element.name.length > 0)
            data += ',';
          for (let i = 0; i < element.name.length; i++) {
            data += element.name[i];
            if (i < element.name.length - 1)
              data += ',';
          }
          console.log("DATA:", data);
          element.name.unshift(value);
          let addTag: Message = {
            feedback: data,
            id: this.indexList[position]
          };
          data = "";

          this.imgService.sendTags(addTag).subscribe((resposeData: any) => {
            let response = JSON.parse(JSON.stringify(resposeData));
            console.log("Response:", response);
            if (response.response == "success") {
              alert("Tags updated successfully");
            }
          });

          this.textT1.unshift(value);
          break;
        }
      }
    }
    event.chipInput!.clear();

  }

  remove(tag: string, index: number): void {
    for (let i = 0; i < this.temp.length; i++) {
      if (this.temp[i].pos == index) {
        for (let j = 0; j < this.temp[i].name.length; j++) {
          if (this.temp[i].name[j] == tag) {
            this.temp[i].name.splice(j, 1);
            this.textT1.splice(j, 1);
            break;
          }
        }

        let data = "";
        for (let j = 0; j < this.temp[i].name.length; j++) {
          data += this.temp[i].name[j];

          if (j != this.temp[i].name.length - 1)
            data += ',';
        }
        let addTag: Message = {
          feedback: data,
          id: this.indexList[index]
        };

        this.imgService.sendTags(addTag).subscribe((resposeData: any) => {
          let response = JSON.parse(JSON.stringify(resposeData));
          console.log("Response:", response);
          if (response.response == "success") {
            alert("Tags updated successfully");
          }
        });

        data = "";
        break;
      }
    }
  }

}
