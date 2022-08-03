import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContactComponent } from './contact.component';
import {ConverterService} from './../shared/converter.service';
import { of } from 'rxjs';

describe('ContactComponent', () => {
  let component: ContactComponent;
  let fixture: ComponentFixture<ContactComponent>;
  let serviceStub: any;

  beforeEach(async () => {

    serviceStub = {
      getContent: () => of('You have been warned'),
    };
    
    await TestBed.configureTestingModule({
      declarations: [ ContactComponent ],
      providers: [ { provide: ConverterService, useValue: serviceStub } ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ContactComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have loading as false', () => {
    expect(component.loading).toBeFalsy();
  });

  it('should have response saying Message successfully sent', () => {
    expect(component.onSubmit).toBeTruthy();
  });

  it('should have invalid email', () => {
    
    let email= component.form.controls.email;
 
    email.setValue('f')
    expect(email.errors).toBeTruthy();
  });
});
