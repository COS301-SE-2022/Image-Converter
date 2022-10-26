import { Component, OnInit,Input } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import {ConverterService} from './../shared/converter.service';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Message } from '../classes/Message';

@Component({
  selector: 'app-shared-image',
  templateUrl: './shared-image.component.html',
  styleUrls: ['./shared-image.component.scss']
})
export class SharedImageComponent implements OnInit {

  image!: string;//hold id of image
  //used for loadig spinner
  loading=false;
  imageUrl!: string;//returned image
  form!: FormGroup;
  
  //These variables are used  in the comment sections
  @Input() commentLabel!: string;
  @Input() hasCancelLabel!: boolean;
  @Input() initialComment: string = "";

  constructor(private _formBuilder: FormBuilder,private _router: Router,private route: ActivatedRoute,private imgService: ConverterService) { }

  ngOnInit(): void {

    this.commentLabel = "Update";    

    this.loading=true;
    //this check the url parameter
    this.route.queryParams
      .subscribe(params => {
        console.log(params); 
        this.image = params.image;
        console.log(this.image); // image
      }
    );

    if(this.image!=undefined && this.image!="")
    {
      localStorage.setItem('imageParam',this.image);
    }
   
    //check if user is logged in
    if(!localStorage.getItem('token') || localStorage.getItem('token')=="")
    {
      this._router.navigateByUrl('/');
    }

    let respsonse:any="";
    //fetch image
    this.imgService.getSharedImage(localStorage.getItem('imageParam')!).subscribe(
      responseData =>{
        localStorage.setItem('imageParam',"");
        
        respsonse = JSON.parse(JSON.stringify(responseData));
         this.imageUrl=respsonse.image;
         this.loading = false;

         this.initialComment=respsonse.comment;
         this.form = this._formBuilder.group({
          comment: [this.initialComment, Validators.required]
        });
      },
       (err) => {
    }
    );
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
      id: this.image
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
