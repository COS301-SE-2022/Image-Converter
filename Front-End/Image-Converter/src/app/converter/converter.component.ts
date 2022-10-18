import { Component, OnInit, HostListener, ViewChild, Input } from '@angular/core';
import {ConverterService} from './../shared/converter.service';
import { Observable, Subscriber } from 'rxjs';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';
import { Message } from '../classes/Message';
import { io, Socket } from 'socket.io-client';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { MatStepper } from '@angular/material/stepper';

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


  //These variables are used  in the comment sections
  @Input() commentLabel!: string;
  @Input() hasCancelLabel!: boolean;
  @Input() initialComment: string = "";
  form!: FormGroup;
  showDim: boolean = false;
  uploadSuccess: boolean = false;
  width!: number;
  height!: number;
  resizedHeight!: number;
  resizedWidth!: number;
  imageID!: any;
  
  //constructor(private imgService: ConverterService,private imgData: ComponentCommunicationService, private _formBuilder: FormBuilder) { }
  socketio: any;
  firstFormGroup = this._formBuilder.group({
    firstCtrl: [''],
  });
  secondFormGroup = this._formBuilder.group({
    secondCtrl: [''],
  });

  @ViewChild('stepper') private myStepper!: MatStepper;
  
  goForward(){
    this.myStepper.next();
}

  myScriptElement!: HTMLScriptElement;
  
  constructor(private _formBuilder: FormBuilder,private imgService: ConverterService,private imgData: ComponentCommunicationService/*,private imageProgress: ImageProcessService*/) 
  { 
    this.myScriptElement = document.createElement("script");
    this.myScriptElement.src = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js";
    document.body.appendChild(this.myScriptElement);

  }

  // variables for file upload
  error: String='';
  dragAreaClass: String='';
  draggedFiles: any;
  myimage?: Observable<any>;

  respsonseBase64!:{image:string};
  saveFile:any='';//used in saveFiles method to save image 
  base64Picture: string ="";
  isDisabled = true;//upload button bool

  //used for loadig spinner
  loading=false;
  loadingPercent=0;

  //to indicate step we are at
  isStep=[false,false,false,false,false]
  isStepCounter=0;

  displayImg: any='../../assets/drag.png';// url of img displayed on upload
  onFileChange(event: any) {// when uploaded using button not drag
    let files: FileList = event.target.files;
    this.uploadSuccess = false;
    this.commentLabel = "Comment"
    
    this.showDim = false


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
      reader.onload = (_event: any) => { 
          this.displayImg = reader.result; 
        const image = new Image();
        image.src = _event.target.result;
        image.onload = (rs: any) => {
          this.height = rs.currentTarget['height'];
          this.width = rs.currentTarget['width'];

        
        };
      }
      console.log(this.width);
      console.log(this.height);
      this.showDim = true;
      this.isDisabled = false;
      this.saveFile=files;
    }
  }

  
  ngOnInit() {
    this.dragAreaClass = 'dragarea';
    //subscribe for communication between components
    this.subscription = this.imgData.currentMessage.subscribe(message => this.message = message);
    this.subscription = this.imgData.currentDisplayDownload.subscribe(dispBool => this.dispBool = dispBool);
   

    this.hasCancelLabel = false;
    this.showDim = false;
    this.uploadSuccess = false;
    this.commentLabel = "Comment"
    this.form = this._formBuilder.group({
      comment: [this.initialComment, Validators.required]
    });
   
    
    // const socket = new WebSocket('http://localhost:5000');

    // // Connection opened
    // socket.addEventListener('open', function (event) {
    //     console.log('Connected to WS Server')
    // });

    // // Listen for messages
    // socket.addEventListener('message', function (event) {
    //     console.log('Message from server ', event.data);
    //     const node = document.createElement("h3");
    //     // Create a text node:
    //     let textnode = document.createTextNode(event.data);
    //     node.appendChild(textnode);
    //     node.appendChild(document.createElement("br"));
    //     document.getElementById("progress")!.appendChild(node);
    // });

    // const sendMessage = () => {
    //     socket.send('Hello From Client1!');
    // }
    this.socketio = io('http://localhost:5000');
    this.socketio.on('data-tmp', (data: any) => {

      console.log(data);
      const node = document.createElement("h3");
        //Create a text node:
        let textnode = document.createTextNode(data);
        node.appendChild(textnode);
        node.appendChild(document.createElement("br"));
        document.getElementById("progress")!.appendChild(node);

        //update loading bar
        this.loadingPercent+=20;
        console.log("per: "+this.loadingPercent);
        document.getElementById("loadingBar")!.style.width ="";
        document.getElementById("loadingBar")!.innerHTML= "";
        document.getElementById("loadingBar")!.style.width = this.loadingPercent+"%";
        document.getElementById("loadingBar")!.innerHTML= this.loadingPercent+"%";

        this.goForward();
      });
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
  //sends uploaded image to the backend for processing.
  saveFiles() {
    this.loadingPercent=0;
    this.loading = true;
    
    if(this.saveFile!=''){
      console.log(this.saveFile[0].size, this.saveFile[0].name, this.saveFile[0].type);

      console.log("Lee  "+this.saveFile[0].name);
      this.convertToBase64(this.saveFile[0]);
      this.myimage?.subscribe(data => {
        // console.log(data);
        
        this.imgService.postImg(data, this.saveFile[0].name).subscribe(
          (responseData: any) =>{
            document.getElementById("progress")!.innerHTML = "";
            this.loading = false;
            this.uploadSuccess = true;
            this.initialComment = ""
            console.log('Res:', responseData['imageHeight'].toString());
            this.resizedHeight = responseData['imageHeight'];
            this.resizedWidth = responseData['imageWidth'];
            this.imageID = responseData['id']
            this.respsonseBase64 = JSON.parse(JSON.stringify(responseData));
             console.log('ResJSn',this.respsonseBase64);
            this.imgData.changeMessage(this.respsonseBase64);
            this.imgData.changBool(true);
            // this.saveFile[0].name;
            // console.log("Omo  "+this.saveFile[0].name);
            document.getElementById("imageFilter")!.style.display = "block";
            (<HTMLInputElement>document.getElementById("commentSection"))!.value = '';
            document.getElementById("conversionFormat")!.style.display = "block";
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
  
  get comment() {  
    return this.form.get('comment');  
  } 

  onComment() {
    console.log('onComment', this.comment!.value);
    this.initialComment = this.comment!.value;
    this.commentLabel = "Update";
    
    let comment: Message = {
      feedback: this.comment!.value,
      id: this.imageID
    };

    this.imgService.sendAnnotations(comment).subscribe(responseData => {
      let response = JSON.parse(JSON.stringify(responseData));

      console.log("Respose:" ,response);
      if(response.response == "success") {
        alert("Comment updated successfully");
      }
    });
  }

}
