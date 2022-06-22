import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of } from 'rxjs';
import { ContactComponent } from './contact.component';
import {ConverterService} from './../shared/converter.service';

describe('ContactComponent', () => {
  let component: ContactComponent;
  let fixture: ComponentFixture<ContactComponent>;

  //used in the stead of real service
  let serviceStub:any;

  beforeEach(async () => {

    serviceStub={
      sendMessage:()=> of('m')
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

  var a;

  it("and so is a spec", function() {
    a = true;

    expect(a).toBe(true);
  });
  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should show loading variable as false (should not be showing loading icon)', () => {
    expect(component.loading).toBeFalsy();
  });
});
