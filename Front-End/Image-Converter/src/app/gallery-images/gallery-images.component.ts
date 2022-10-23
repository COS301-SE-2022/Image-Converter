import { Component, OnInit } from '@angular/core';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';
import { COMMA, ENTER  } from '@angular/cdk/keycodes';
import { MatChipInputEvent } from '@angular/material/chips';
import {ConverterService} from './../shared/converter.service';
import {MatDialogRef,MatDialog,MatDialogConfig} from '@angular/material/dialog';
import { ImagePopupComponent } from '../image-popup/image-popup.component';
import { Validators } from '@angular/forms';
import {Message} from "../classes/Message";


export interface Tag {
  name: string;
}

export interface TagList {
  pos: number;
  name: any[];
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
  loading=false;
  dash: string = "-";


  //holds processed images
  uploadedImgProcessed: string[] = [];
  commentList: string[] = [];
  indexList: number[] = [];
  temp: TagList[] = [];

  // ["line graph","test graph", "name3", "name4", "name5", "name6", "name7" ,"name8", "name9"];
  // ["16 Oct","random tag", "tag3", "tag4", "tag5", "tag6","tag7", "tag8", "tag9"];
  nameArr: string[] = [];
  tagArr: string[] = [];
  dateArr:string[] = [];
  tags: string[] = [];


  textT1: any[] = [];
  uuid:BigInteger[]=[];
  constructor(private dialog: MatDialog, private graphFolderData: ComponentCommunicationService,private imgService: ConverterService) { }

  ngOnInit(): void {
    this.subscription = this.graphFolderData.currentGraph.subscribe(selectedFolder => this.selectedFolder = selectedFolder);
    this.loading = true;

    if(this.selectedFolder == "Line graphs")
      this.selectedFolder = "line graph";
    else if(this.selectedFolder == "Bar graphs")
      this.selectedFolder = "bar graph";
    else if(this.selectedFolder == "Pie charts")
      this.selectedFolder = "pie chart";
    else if(this.selectedFolder == "Tables")
      this.selectedFolder = "table";
    else if(this.selectedFolder == "Flow charts")
      this.selectedFolder = "flow chart";


    this.imgService.GraphGallaryData(this.selectedFolder).subscribe(
      responseData =>{
        this.loading = false;
        let respsonseBase64 = JSON.parse(JSON.stringify(responseData));
        console.log("Gallery:", respsonseBase64);

        for(let i=0;i<9;i++){ // respsonseBase64.OriginalImage.length

            this.uploadedImgProcessed.push(respsonseBase64.proccesedImage[i]);
            this.commentList.push(respsonseBase64.Comments[i]);
            this.indexList.push(respsonseBase64.Index[i]);
            this.tagArr.push(respsonseBase64.Tags[i]);
            this.nameArr.push(respsonseBase64.Names[i]);
            console.log("index: "+respsonseBase64.Tags[i]);

           // this.uuid.push(respsonseBase64.Index[i]);
        }
        let textT: string[] = [];

        let data: string;
        for (let index = 0; index < this.tagArr.length; index++) {
          let words = this.tagArr[index];
          data = "";
          let num = 0;
          for (let j = 0; j < words.length && num < 4; j++) {
            if(words[j] == '{' || words[j] == '}' || words[j] == ' ')
              continue;
            else if(words[j] != ',')
              data += words[j];
            else if(words[j] == ',') {
              textT.push(data);
              this.textT1.push(data);
              data = '';
              num++;
            }
          }

          this.temp.push({pos: index, name: textT, tags: [1, 2, 3, 4]});
          textT = [];
          // textT.push(data);
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

  text: string='';
  check: string = this.text.replace(/[^a-zA-Z ]/g,"");
  flag: boolean = true;
  ser: any;
  textEntered(searchVal: string) {
    this.text = searchVal.replaceAll(/[^\w\s.]/gi,' ');
  }

  textT: string='';

  //Image tags
  addOnBlur = true;
  readonly separatorKeysCodes = [ENTER, COMMA] as const;


  addT: string[] = [];
  add(event: MatChipInputEvent, position: number): void {
    console.log("TagNum", position)
    const value = (event.value || '').trim();


    if (value) {
      for (const element of this.temp) {
        if (element.pos == position) {
          console.log(this.indexList[position]);
          element.name.unshift(value);
          let data = "";
          for (let i = 0; i < element.name.length; i++) {
            data += element.name;

            if(i != element.name.length - 1)
              data += ',';
          }

          let addTag: Message = {
            feedback: value,
            id: this.indexList[position]
          };

          this.imgService.sendTags(addTag).subscribe((resposeData: any) => {
              let response = JSON.parse(JSON.stringify(resposeData));
              console.log("Response:", response);
            if(response.response == "success") {
              alert("Tags updated successfully");
            }
          });

          this.textT1.unshift(value);
          break;
        }
      }
    }

    // Clear the input value
    event.chipInput!.clear();

  }

  remove(tag: string, index: number): void {
    console.log(this.indexList[index]);
    console.log("Ren",index)
    for (let i = 0; i < this.temp.length; i++) {
      if(this.temp[i].pos == index) {
        for (let j = 0; j < this.temp[i].name.length; j++) {
          if(this.temp[i].name[j] == tag) {
            this.temp[i].name.splice(j, 1);
            this.textT1[i].splice(j, 1);

            break;
          }
        }
        break;
      }
    }
  }

}
