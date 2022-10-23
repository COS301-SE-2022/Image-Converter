import { Component, Inject, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef,MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Message } from '../classes/Message';
import { ConverterService } from '../shared/converter.service';
import { UploadHistoryComponent } from '../upload-history/upload-history.component';

@Component({
  selector: 'app-image-popup',
  templateUrl: './image-popup.component.html',
  styleUrls: ['./image-popup.component.scss']
})
export class ImagePopupComponent implements OnInit {
  //These variables are used  in the comment sections
  @Input() commentLabel: string = "Update";
  @Input() initialComment: string = "";
  form!: FormGroup;
  uploadSuccess: boolean = false;
  imageID!: any;
  
  //holds the url of the image passed into this component
  imageUrl!: string;
  imageProcessedUrl!: string;
  

  constructor(private imgService: ConverterService, @Inject(MAT_DIALOG_DATA) public data: {img: string,imgProcessed:string, comment:string, index:number},public dialogRef: MatDialogRef<UploadHistoryComponent>, private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.imageUrl=this.data.img;
    this.imageProcessedUrl=this.data.imgProcessed;
    console.log("Data:", this.data);
    this.initialComment= this.data.comment;
    this.imageID=this.data.index;

    console.log(this.imageUrl);

    this.uploadSuccess = false;
    this.commentLabel = "Update"
    this.form = this.formBuilder.group({
      comment: [this.initialComment, Validators.required]
    });
  }

  get comment() {  
    return this.form.get('comment');  
  } 

  onComment(): void {
    console.log('onComment', this.comment!.value);
    this.initialComment = this.comment!.value;
    this.commentLabel = "Update";
    
    let comment: Message = {
      feedback: this.comment!.value,
      id : this.imageID
    };

    this.imgService.sendAnnotations(comment).subscribe(responseData => {
      let response = JSON.parse(JSON.stringify(responseData));

      console.log("Respose:" ,response);
      if(response.response == "success") {
        alert("Comment updated successfully");
      }
    });
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
}
