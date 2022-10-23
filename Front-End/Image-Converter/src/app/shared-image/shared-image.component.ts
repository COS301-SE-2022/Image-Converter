import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-shared-image',
  templateUrl: './shared-image.component.html',
  styleUrls: ['./shared-image.component.scss']
})
export class SharedImageComponent implements OnInit {

  imgage!: string;

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {

    //this check the url parameter
    this.route.queryParams
      .subscribe(params => {
        console.log(params); // { orderby: "price" }
        this.imgage = params.imgage;
        console.log(this.imgage); // price
      }
    );

  }

}
