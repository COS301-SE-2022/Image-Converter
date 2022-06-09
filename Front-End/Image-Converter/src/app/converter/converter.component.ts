import { Component, OnInit, HostListener } from '@angular/core';
import {ConverterService} from './../shared/converter.service';
import { Observable, Subscriber } from 'rxjs';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-converter',
  templateUrl: './converter.component.html',
  styleUrls: ['./converter.component.scss']
})
export class ConverterComponent implements OnInit {

  //these variables are used for the communication between converter and filter components
  message!: string;
  dispBool!: boolean;
  subscription!: Subscription;
  
  constructor(private imgService: ConverterService,private imgData: ComponentCommunicationService) { }

  // variables for file upload
  error: String='';
  dragAreaClass: String='';
  draggedFiles: any;
  myimage?: Observable<any>;

  respsonseBase64!:{image:string};
  saveFile:any='';//used in saveFiles method to save image 
  base64Picture: string ="";
  isDisabled = true;//upload button bool

  displayImg: any='../../assets/drag.png';// url of img displayed on upload
  onFileChange(event: any) {// when uploaded using button not drag
    let files: FileList = event.target.files;
   // this.saveFiles(files);
    
    this.checkifImg(files);
      if(this.error == '')
      {
        const mimeType = files[0].type;
      if (mimeType.match(/image\/*/) == null) {
        this.error = "Only images are supported.";
        return;
      }

      const reader = new FileReader();
      let imagePath = files;
      let url;
      reader.readAsDataURL(files[0]); 
      reader.onload = (_event) => { 
          this.displayImg = reader.result; 
      }
        this.isDisabled = false;
        this.saveFile=files;
      }
  }

  ngOnInit() {
    this.dragAreaClass = 'dragarea';
    //subscribe for communication between components
    this.subscription = this.imgData.currentMessage.subscribe(message => this.message = message);
    this.subscription = this.imgData.currentDisplayDownload.subscribe(dispBool => this.dispBool = dispBool);

  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

  @HostListener('dragover', ['$event']) onDragOver(event: any) {
    this.dragAreaClass = 'droparea';
    event.preventDefault();
  }

  @HostListener('dragenter', ['$event']) onDragEnter(event: any) {
    this.dragAreaClass = 'droparea';
    event.preventDefault();
  }
  @HostListener('dragend', ['$event']) onDragEnd(event: any) {
    this.dragAreaClass = 'dragarea';
    event.preventDefault();
  }

  @HostListener('dragleave', ['$event']) onDragLeave(event: any) {
    this.dragAreaClass = 'dragarea';
    event.preventDefault();
  }
  
  @HostListener('drop', ['$event']) onDrop(event: any) {
    this.dragAreaClass = 'dragarea';
    event.preventDefault();
    event.stopPropagation();
    if (event.dataTransfer.files) {
      let files: FileList = event.dataTransfer.files;
      
      
      this.checkifImg(files);
      if(this.error == '')
      {
        const mimeType = files[0].type;
      if (mimeType.match(/image\/*/) == null) {
        this.error = "Only images are supported.";
        return;
      }

      const reader = new FileReader();
      let imagePath = files;
      let url;
      reader.readAsDataURL(files[0]); 
      reader.onload = (_event) => { 
          this.displayImg = reader.result; 
      }
        this.isDisabled = false;
         this.saveFile=files;
      }
    }
  }

  //check if uploaded file is an image
  checkifImg(files: FileList)
  {
    //to implement
    if (files.length > 1) this.error = 'Only one image a at time allow';
    else {
      this.error = '';
      console.log(files[0].size, files[0].name, files[0].type);
      this.draggedFiles = files;
      console.log(files);
    }
  }
  saveFiles() {
    if(this.saveFile!=''){
      console.log(this.saveFile[0].size, this.saveFile[0].name, this.saveFile[0].type);

      console.log("Lee  "+this.saveFile[0].name);
      this.convertToBase64(this.saveFile[0]);
      this.myimage?.subscribe(data => {
        // console.log(data);
        this.imgService.postImg(data).subscribe(
          responseData =>{
            console.log(responseData);
            this.respsonseBase64 = JSON.parse(JSON.stringify(responseData));
            // console.log(this.respsonseBase64);
            this.imgData.changeMessage(this.respsonseBase64.image);
            this.imgData.changBool(true);
          }
        );
      });
    }
  }

  convertToBase64(file: File) {
    this.myimage = new Observable((subscriber: Subscriber<any>) => {
      this.readFile(file, subscriber);
    });
  }

  readFile(file: File, subscriber: Subscriber<any>) {
    const filereader = new FileReader();
    filereader.readAsDataURL(file);

    filereader.onload = () => {
      subscriber.next(filereader.result);
      subscriber.complete();
    };
    filereader.onerror = (error) => {
      subscriber.error(error);
      subscriber.complete();
    };
  }

}
