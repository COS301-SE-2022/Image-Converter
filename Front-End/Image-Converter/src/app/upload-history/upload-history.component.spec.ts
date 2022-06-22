import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UploadHistoryComponent } from './upload-history.component';
import {ConverterService} from './../shared/converter.service';


describe('UploadHistoryComponent', () => {
  let component: UploadHistoryComponent;
  let fixture: ComponentFixture<UploadHistoryComponent>;

    //used in the stead of real service
  let serviceStub:any;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UploadHistoryComponent ],
      providers: [ { provide: ConverterService, useValue: serviceStub } ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UploadHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
