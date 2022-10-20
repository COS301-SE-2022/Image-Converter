import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ComponentCommunicationService {

  private messageSource = new BehaviorSubject('default message');
  currentMessage = this.messageSource.asObservable();

  private displayDownload = new BehaviorSubject(false);
  currentDisplayDownload = this.displayDownload.asObservable();

  private imgFilter = new BehaviorSubject('revert');// this is sent to the image convertion buttons
  currentimgFilter = this.imgFilter.asObservable();
  
  private typeOfGraph = new BehaviorSubject('none');// this shows the name of the folder 
  currentGraph= this.typeOfGraph.asObservable();

  private resizedHeight = new BehaviorSubject('none');// this shows the name of the folder 
  currentHeight= this.resizedHeight.asObservable();

  private resizedWidth = new BehaviorSubject('none');// this shows the name of the folder 
  currentWidth= this.resizedWidth.asObservable();

  constructor() { }

  //used to change message between components
  changeMessage(message: any) {
    this.messageSource.next(message)
  }
  changBool(m :boolean){
    this.displayDownload.next(m);
  }

  changeFilter(filter: any){
    this.imgFilter.next(filter)
  }
  changeGraphFolder(folder: any){
    this.typeOfGraph.next(folder)
  }

  changeWidth(width: any){
    this.resizedWidth.next(width)
  }

  changeHeight(height: any){
    this.resizedHeight.next(height)
  }
}
