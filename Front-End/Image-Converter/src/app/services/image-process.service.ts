import { Injectable } from '@angular/core';
import { WebsocketService } from './websocket.service';
import { map,Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ImageProcessService {
  
  messages: Subject<any>;

  // Our constructor calls our wsService connect method
  constructor(private wsService: WebsocketService) {
    this.messages = <Subject<any>>wsService
      .connect().pipe(
      map((response: any): any => {
        return response;
      }))
   }
}
