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
}
