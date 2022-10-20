import { Component, OnInit } from '@angular/core';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';
import { COMMA, ENTER  } from '@angular/cdk/keycodes';
import { MatChipInputEvent } from '@angular/material/chips';
import {ConverterService} from './../shared/converter.service';
import {MatDialogRef,MatDialog,MatDialogConfig} from '@angular/material/dialog';
import { ImagePopupComponent } from '../image-popup/image-popup.component';
import { Validators } from '@angular/forms';

export interface Tag {
  name: string;
}


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
  commentList: string[] = [];
  indexList: number[] = [];
  // ["line graph","test graph", "name3", "name4", "name5", "name6", "name7" ,"name8", "name9"];
  // ["16 Oct","random tag", "tag3", "tag4", "tag5", "tag6","tag7", "tag8", "tag9"];
  nameArr: string[] = [];
  tagArr: string[] = [];
  dateArr:string[] = [];
  tags: Tag[] = [];
  tags4: string[] = ['', '', '', ''];


  uuid:BigInteger[]=[];
  constructor(private dialog: MatDialog, private graphFolderData: ComponentCommunicationService,private imgService: ConverterService) { }

  ngOnInit(): void {
    this.subscription = this.graphFolderData.currentGraph.subscribe(selectedFolder => this.selectedFolder = selectedFolder);
    this.loading = true;
    // console.log("in gallery top");
    console.log(this.selectedFolder);

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
        // console.log("in gallery");
        this.loading = false;
        let respsonseBase64 = JSON.parse(JSON.stringify(responseData));
        console.log("Gallery:", respsonseBase64);
      //  console.log("response here: "+JSON.stringify(responseData));

        for(let i=0;i<9;i++){ // respsonseBase64.OriginalImage.length

            this.uploadedImgProcessed.push(respsonseBase64.proccesedImage[i]);
            this.commentList.push(respsonseBase64.Comments[i]);
            this.indexList.push(respsonseBase64.Index[i]);
            this.tagArr.push(respsonseBase64.Tags[i]);
            this.nameArr.push(respsonseBase64.Names[i]);
            // console.log("index: "+respsonseBase64.Tags[i]);
            
           // this.uuid.push(respsonseBase64.Index[i]);
        }
        let textT: string[] = [];
        let data: string;
        for (let index = 0; index < this.tagArr.length; index++) {
          console.log(this.tagArr[index]);
          let words = this.tagArr[index];
          data = "";
          let num: number;
          num = 0;
          for (let j = 0; j < words.length && num < 4; j++) {
            //  console.log(words[j]);
            if(words[j] == '{' || words[j] == '}')
            continue;
            else if(words[j] != ',')
              data += words[j];
            else if(words[j] == ',') {
              if(num < 3)
                data += ',';
              num += 1;
            }
          }
          textT.push(data);  
        }
        console.log(textT);
        for (let index = 0; index < textT.length; index++) {
          this.tags.push({name: textT[index]})
          
          
        }
        textT = [];
        let s = '';
        for (let i = 0; i < this.tags.length; i++) {
          let w = this.tags[i].name;
          s = "";
          for (let j = 0; j < w.length; j++) {
            if(w[j] != ',')
              s += w[j];
            else if(w[j] == ',') {
              textT.push(s);
              s = ''
            }
              
          }
          textT.push(s)
        }
        console.log(textT);
        this.tags = []
        for (let index = 0; index < textT.length; index++) {
          this.tags.push({name: textT[index]})
          
          
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

  textEntered(searchVal: string){
    this.text = searchVal.replaceAll(/[^\w\s.]/gi,' ');
    console.log(this.text);
  }

  textT: string='';
  
  
  // textT = "";
  // for (let= 0; i < this.tagArr; i++) {
  //    let words = this.tagArr[i];
  //     if(words[i] == '{' || words[i] == '}')
  //       continue;
  //     else if(words[i] != ',')
  //       textT += words[i];
  //     else if(words[i] == ',')
  //       textT += ',';        
  // }
  // this.tagArr.push(textT);

  //Image tags
  addOnBlur = true;
  readonly separatorKeysCodes = [ENTER, COMMA] as const;
  
  
  addT: string[] = [];
  add(event: MatChipInputEvent): void {
    const value = (event.value || '').trim();

    // Add our fruit
    if (value) {
      this.tags.unshift({name: value})
      this.tagArr.unshift(value)
    }

    // Clear the input value
    event.chipInput!.clear();
  }

  remove(tag: Tag): void {
    const index = this.tags.indexOf(tag);

    if (index >= 0) {
      this.tags.splice(index, 1);
    }
  }

}
