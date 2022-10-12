import { Component, OnInit } from '@angular/core';
import { ComponentCommunicationService } from './../shared/component-communication.service';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss']
})
export class GalleryComponent implements OnInit {

  constructor(private graphFolderData: ComponentCommunicationService,private _router: Router) { }

  graphNames=["Line","Bar","Chart","graph","graph","graph"];
  subscription!: Subscription;
  selectedFolder!: String;
  ngOnInit(): void {
    this.subscription = this.graphFolderData.currentGraph.subscribe(selectedFolder => this.selectedFolder = selectedFolder);
  }

  //opens folder of selected graphs
  fileSelection(name:string){
    this.graphFolderData.changeGraphFolder(name);
    this._router.navigateByUrl('/nav/galleryimages');
  }
}
