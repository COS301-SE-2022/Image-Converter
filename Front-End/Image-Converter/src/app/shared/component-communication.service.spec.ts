import { TestBed } from '@angular/core/testing';

import { ComponentCommunicationService } from './component-communication.service';

describe('ComponentCommunicationService', () => {
  let service: ComponentCommunicationService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ComponentCommunicationService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  const msg = 'defualt message'
  // it('changeMessage', ()=>{
  //   expect(service.changeMessage(msg)).not.toEqual(service.messageSource.next(msg));
  // });




});
