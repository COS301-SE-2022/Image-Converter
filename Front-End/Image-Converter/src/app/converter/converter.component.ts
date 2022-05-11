import { Component, OnInit, HostListener } from '@angular/core';

@Component({
  selector: 'app-converter',
  templateUrl: './converter.component.html',
  styleUrls: ['./converter.component.scss']
})
export class ConverterComponent implements OnInit {

  constructor() { }

  

  // variables for file upload
  error: String='';
  dragAreaClass: String='';
  draggedFiles: any;
  
  //upload button bool
  isDisabled = true;

  displayImg: any='../../assets/drag.png';// url of img displayed on upload
  onFileChange(event: any) {// when uploaded using button not drag
    let files: FileList = event.target.files;
    this.saveFiles(files);
    const mimeType = files[0].type;
      if (mimeType.match(/image\/*/) == null) {
        //this.message = "Only images are supported.";
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
      
      const mimeType = files[0].type;
      if (mimeType.match(/image\/*/) == null) {
        //this.message = "Only images are supported.";
        return;
    }

    const reader = new FileReader();
    let imagePath = files;
    let url;
    reader.readAsDataURL(files[0]); 
    reader.onload = (_event) => { 
        this.displayImg = reader.result; 
    }
      this.saveFiles(files);
      this.isDisabled = false;
    }
  }

  //check if uploaded file is an image
  checkifImg()
  {
    //to implement
  }
  saveFiles(files: FileList) {
    if (files.length > 1) this.error = 'Only one file at time allow';
    else {
      this.error = '';
      console.log(files[0].size, files[0].name, files[0].type);
      this.draggedFiles = files;
      console.log(files);
    }
  }

}
