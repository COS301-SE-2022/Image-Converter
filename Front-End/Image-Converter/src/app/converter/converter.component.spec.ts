import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of } from 'rxjs';
import { RouterTestingModule } from '@angular/router/testing'
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentCommunicationService } from '../shared/component-communication.service';
import { ConverterService } from '../shared/converter.service';
import { ConverterComponent } from './converter.component';

describe('ConverterComponent', () => {
  // Prepare mock services
  let communicationStub: any;
  let converterStub: any;

  //Prepare the component and its fixture
  let component: ConverterComponent;
  let fixture: ComponentFixture<ConverterComponent>;

  beforeEach(async () => {
    TestBed.configureTestingModule({
      imports: [
        RouterTestingModule,
        HttpClientTestingModule, 
      ],
      declarations: [ 
        ConverterComponent
      ],
      providers: [
        ConverterService,
        ComponentCommunicationService
      ]
    }).compileComponents();
  });

  beforeEach(async () => {
    fixture = TestBed.createComponent(ConverterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });
  
  it('should create the converter compenent', async() => {
    expect(component).toBeTruthy();
  });

  describe('loading attribute', async() => {
    it('should expect the loading attribute to be false', async() => {
      expect(component.loading).toBeFalsy();
    });
  });

  describe('default isDisabled attribute value', async() => {
    it('should expect the isDisabled attribute to be true', async() => {
      expect(component.isDisabled).toBeTruthy();
    });
  });

  describe('default error attribute value', async() => {
    it('should expect the error attribute to be \'\'', async() => {
      expect(component.error).toMatch("");
    });
  });

  describe('testing checkifImg fuction', async() => {
    const blob = new Blob([""], { type: "text/html" });
    const file = <File>blob;
    const fileList: FileList = {
      0: file,
      length: 1,
      item: (index: number) => file
    };
    it('should expect the error attribute to be \'\'', () => {
      component.checkifImg(fileList);
      expect(component.error).toEqual('');
    });
  });

  describe('testing checkifImg fuction, with more than one file', async() => {
    const blob = new Blob([""], { type: "text/html" });
    const file = <File>blob;
    const fileList: FileList = {
      0: file,
      1: file,
      length: 2,
      item: (index: number) => file
    };
    it('should expect the error attribute to be \'Only one image a at time allow\'', () => {
      component.checkifImg(fileList);
      expect(component.error).toEqual('Only one image a at time allow');
    });
  });

});
