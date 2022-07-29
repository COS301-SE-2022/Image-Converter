import { Component, OnInit } from '@angular/core';
import {FormGroup,FormControl,Validators} from '@angular/forms';
import {ConverterService} from './../shared/converter.service';

@Component({
  selector: 'app-graph-plotting',
  templateUrl: './graph-plotting.component.html',
  styleUrls: ['./graph-plotting.component.scss']
})
export class GraphPlottingComponent implements OnInit {

  constructor(private  graphPService: ConverterService,) { }

  //used for loadig spinner
  loading=false;
  display=false;
  ngOnInit(): void {
  }

  form = new FormGroup({  
    formula: new FormControl('', Validators.required)
  });

  get formula() {  
    return this.form.get('formula');  
  } 

  displayImg:any;
  //handle formula submission then displays drawn graph
  onFomulaSubmit()
  {
    this.loading = true;
    let formula = {
      formula : this.form.get('formula')!.value
    } 
    let response:any=null;
    this.graphPService.postFormula(formula).subscribe(
      responseData =>{
          this.loading = false;
            //response
            response = JSON.parse(JSON.stringify(responseData));
            console.log(response);
            if(response.image){
              console.log("success: "+response.image);
              this.displayImg=response.image;
              this.display=true;
              
            }
            else{
              alert("could not draw graph");
            }
        }
    );
  }

  /*downloadFile(imageDownload:any) {
    var a = document.createElement('a');
    a.href = imageDownload;

    console.log("a.href: "+a.href)
    // this.download(a.href)
    // console.log("a.download: "+a.download)
    a.download = "output.png";
     document.body.appendChild(a);
     a.click();
     document.body.removeChild(a);

  }
*/
  downloadFile(imageDownload:any)
  {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", imageDownload, true);
    xhr.responseType = "blob";
    xhr.onload = function(){
        var urlCreator = window.URL || window.webkitURL;
        var imageUrl = urlCreator.createObjectURL(this.response);
        var tag = document.createElement('a');
        tag.href = imageUrl;
        tag.download = "output.png";
        document.body.appendChild(tag);
        tag.click();
        document.body.removeChild(tag);
    }
    xhr.send();
  }


  // download(source:any){
  //   const fileName = source.split('/').pop();
	// var el = document.createElement("a");
	// el.setAttribute("href", source);
	// el.setAttribute("download", fileName);
	// document.body.appendChild(el);
 	// el.click();
	// el.remove();
// }


  
}
