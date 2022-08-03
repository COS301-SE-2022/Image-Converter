import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing'
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ImagePopupComponent } from './image-popup.component';
import {UploadHistoryComponent } from '../upload-history/upload-history.component';

describe('ImagePopupComponent', () => {
  let component: ImagePopupComponent;
  let fixture: ComponentFixture<ImagePopupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ImagePopupComponent ] ,
      imports: [
        RouterTestingModule,
        HttpClientTestingModule, 
      ],
      providers: [
        UploadHistoryComponent
      ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ImagePopupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create image pop up component', () => {
    expect(component).toBeTruthy();
  });

  describe('testing downloadFile method', async() => {
    const blob = new Blob([""], { type: "text/html" });
    const file = <File>blob;
    it('', () => {
      component.downloadFile(file);
      // expect(component).toEqual('');
    });
  });

  describe('testing deleteImages method', async() => {
    const blob = new Blob([""], { type: "text/html" });
    const file = <File>blob;
    it('', () => {
      component.deleteImages();
      // expect(component).toEqual('');
    });
  });

});
