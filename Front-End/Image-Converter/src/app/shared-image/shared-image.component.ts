import { Component, OnInit } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-shared-image',
  templateUrl: './shared-image.component.html',
  styleUrls: ['./shared-image.component.scss']
})
export class SharedImageComponent implements OnInit {

  image!: string;
  //used for loadig spinner
  loading=false;
  imageUrl!: string;//returned image
  
  constructor(private _router: Router,private route: ActivatedRoute,private imgService: ConverterService) { }

  ngOnInit(): void {
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
    if(!localStorage.getItem('token') && localStorage.getItem('token')=="")
    {
      this._router.navigateByUrl('/');
    }

    let respsonse:any="";
    //fetch image
    this.imgService.getSharedImage(localStorage.getItem('imageParam')!).subscribe(
      responseData =>{
        localStorage.setItem('imageParam',"");
        this.loading = false;
        respsonse = JSON.parse(JSON.stringify(responseData));

         this.imageUrl=respsonse.Image;
      },
       (err) => {
    }
    );
  }

}
