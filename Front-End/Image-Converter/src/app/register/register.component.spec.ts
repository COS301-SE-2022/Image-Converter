import { HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ReactiveFormsModule } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';

import { RegisterComponent } from './register.component';

describe('RegisterComponent', () => {
  let component: RegisterComponent;
  let fixture: ComponentFixture<RegisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegisterComponent ],
      imports: [ReactiveFormsModule, HttpClientTestingModule, RouterTestingModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('title is correct', () => {

    expect(component.title).toBe('reactiveformproject')
    // expect(component.title).toBe('omo')
  });


  it('hide is true', () => {

    expect(component.hide).toBeTruthy();
    // expect(component.
  
  });

  it('email - should be valid', () => {

    let mail = component.registerForm.controls.email
    expect(mail.valid).toBeFalsy();
    expect(mail.pristine).toBeTruthy();
    // expect(mail.errors.required).toBeTruthy();

    mail.setValue('omo')
    // expect(mail.errors.email).toBeTruthy


  });

  it('email - should check if correct email adress is entered', () => {

    let mail = component.registerForm.controls.email
    mail.setValue('abc@gmail.com')
    // expect(mail.errors.email).toBeNull()
  });


  it('should check for password errors', () => {

    let pwd = component.registerForm.controls.password;
    expect(pwd.errors).toBeTruthy();
    pwd.setValue('0123456');
    expect(pwd.errors).toBeTruthy();//.minLength  
  });


  it('should check for password validity', () => {

    let pwd = component.registerForm.controls.password;
    pwd.setValue('0123456789');
    expect(pwd.errors).toBeNull();
    expect(pwd.errors).toBeFalsy();
    expect(pwd.valid).toBeTruthy();//.minLength  
  });
});
