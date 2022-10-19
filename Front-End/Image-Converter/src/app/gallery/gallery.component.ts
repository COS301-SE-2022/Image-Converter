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

  subscription!: Subscription;
  selectedFolder!: String;
  ngOnInit(): void {
    this.subscription = this.graphFolderData.currentGraph.subscribe(selectedFolder => this.selectedFolder = selectedFolder);
  }

  //opens folder of selected graphs
  fileSelection(name:string){
    console.log("GraphName: ", name)
    let graphName = ""
    if(name == "line graph")
      graphName = "Line graphs"
    else if(name == "bar graph")
      graphName = "Bar graphs";
    else if(name == "pie chart")
      graphName = "Pie charts";
    else if(name == "table")
      graphName = "Tables";
    else if(name == "flow chart")
      graphName = "Flow charts";
    this.graphFolderData.changeGraphFolder(graphName);
    this._router.navigateByUrl('/nav/galleryimages');
    
  }

  onSubmitLineGraphs(){
    this._router.navigateByUrl('/nav/galleryimages');
  }
}
