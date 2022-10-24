import { Component, OnInit, Inject,Input } from '@angular/core';
import { MatDialogRef,MAT_DIALOG_DATA,MatDialog } from '@angular/material/dialog';


@Component({
  selector: 'app-link-popup',
  templateUrl: './link-popup.component.html',
  styleUrls: ['./link-popup.component.scss']
})
export class LinkPopupComponent implements OnInit {
  url!:string;
  constructor(@Inject(MAT_DIALOG_DATA) public data: {url:string}) { }

  ngOnInit(): void {
    this.url=this.data.url;
  }

}
