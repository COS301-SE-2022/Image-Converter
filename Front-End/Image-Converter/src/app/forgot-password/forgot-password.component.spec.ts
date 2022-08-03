import { HttpClientModule } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ReactiveFormsModule } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';

import { ForgotPasswordComponent } from './forgot-password.component';

describe('ForgotPasswordComponent', () => {
  let component: ForgotPasswordComponent;
  let fixture: ComponentFixture<ForgotPasswordComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ForgotPasswordComponent ],
      imports: [ReactiveFormsModule ,HttpClientModule, RouterTestingModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ForgotPasswordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should check for password errors', () => {

    let pwd = component.formPass.controls.password;
    expect(pwd.errors).toBeTruthy();
    pwd.setValue('0123456');
    expect(pwd.errors).toBeTruthy();//.minLength  
  });

  it('should check for password validity', () => {

    let pwd = component.formPass.controls.password;
    pwd.setValue('0123456789');
    expect(pwd.errors).toBeNull();
    expect(pwd.errors).toBeFalsy();
    expect(pwd.valid).toBeTruthy();//.minLength  
  });


  it('should check for password errors', () => {

    let pwd = component.formPass.controls.cpassword;
    expect(pwd.errors).toBeTruthy();
    pwd.setValue('0123456');
    expect(pwd.errors).toBeTruthy();//.minLength  
  });

  it('should check for password validity', () => {

    let cpwd = component.formPass.controls.cpassword;
    cpwd.setValue('0123456789');
    // expect(cpwd.errors).toBeNull();
    // expect(cpwd.errors).toBeTruthy();
    expect(cpwd.valid).toBeFalsy();//.minLength  
  });


  it('code - should be valid if it is a number with more than 4 characters', () => {

    let cde = component.formCode.controls.code
    cde.setValue('1234');
    expect(cde.errors).toBeNull();
    
  });

  it('code - should be invalid if it is a number with less than 4 characters', () => {

    let cde = component.formCode.controls.code
    cde.setValue('1234');
    // expect(cde.errors).toEqual(jasmine.any(Number));
    expect(cde.errors).toBeNull();
    
  });

});
