import { Component, OnInit } from '@angular/core';
import { ConverterService } from '../shared/converter.service';

@Component({
  selector: 'app-unrecognized-images',
  templateUrl: './unrecognized-images.component.html',
  styleUrls: ['./unrecognized-images.component.scss']
})
export class UnrecognizedImagesComponent implements OnInit {

  constructor(private imgService: ConverterService) { }
    //holds unprocessed images
    uploadedImg: string[] = [];
    //holds unprocessed images
    uploadedImgProcessed: string[] = [];
  
    uuid:BigInteger[]=[];
    //used for loadig spinner
    loading=false;
  ngOnInit(): void {
    this.loading = true;
    let respsonseBase64:any="";
      this.imgService.getUnrecognizedGraphs().subscribe(
        responseData =>{
          this.loading = false;
           respsonseBase64 = JSON.parse(JSON.stringify(responseData));

         //console.log("response here: "+JSON.stringify(responseData));
         
          for(let i=0;i<respsonseBase64.OriginalImage.length;i++){

              this.uploadedImg.push(respsonseBase64.OriginalImage[i]);
              this.uploadedImgProcessed.push(respsonseBase64.proccesedImage[i]);
              console.log("index: "+respsonseBase64.Index[i]);
              this.uuid.push(respsonseBase64.Index[i]);
          }
        },//code below ensures that if token is invalid or expired user gets sent back to login
         (err) => {
          //if (err === 'Unauthorized') { this._router.navigateByUrl('/'); }
      }
      );
  }


}
