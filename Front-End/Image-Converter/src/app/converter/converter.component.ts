import { Component, OnInit, HostListener } from '@angular/core';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-converter',
  templateUrl: './converter.component.html',
  styleUrls: ['./converter.component.scss']
})
export class ConverterComponent implements OnInit {

  constructor(private imgService: ConverterService) { }

  

  // variables for file upload
  error: String='';
  dragAreaClass: String='';
  draggedFiles: any;
  
  saveFile:any='';//used in saveFiles method to save image 

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
      this.imgService.postImg(this.saveFile[0]).subscribe(
        data =>{
          console.log('done');
          //Image.value = null;
          //this.imageUrl = "/assets/img/default-image.png";
        }
      );
    }
  }

}
