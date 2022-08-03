import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConversionComponent } from './conversion.component';
import { ComponentCommunicationService } from './../shared/component-communication.service';

import { of } from 'rxjs';

describe('ConversionComponent', () => {
  let component: ConversionComponent;
  let fixture: ComponentFixture<ConversionComponent>;

  let serviceStub: any;

  beforeEach(async () => {

    serviceStub={}
    await TestBed.configureTestingModule({
      declarations: [ ConversionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConversionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

 /* it('should have message with "download png"', () => {
    expect(component.content).toContain('warn');
  });*/

  
  it('should have message with "default message" from ComponentCommunicationService', () => {
    expect(component.message).toContain('default message');
  });

  it('should download png', () => {
    expect(component.downloadPngFile).toBeTruthy();
  });
  it('should download jpg', () => {
    expect(component.downloadJpgFile).toBeTruthy();
  });

  it('should have dispBool false from ComponentCommunicationService', () => {
    expect(component.dispBool).toBeFalsy();;
  });
});
