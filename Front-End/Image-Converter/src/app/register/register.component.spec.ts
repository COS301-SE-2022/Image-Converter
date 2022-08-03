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

  it('username should be invalid if it is less than 2 characters', () => {

    let nme = component.registerForm.controls.name
    nme.setValue('O');
    expect(nme.errors).toBeTruthy();
  
  });

  it('username should be valid if it is more than 2 characters', () => {

    let nme = component.registerForm.controls.name
    nme.setValue('Omo');
    expect(nme.errors).toBeFalsy();
  
  });

  it('surname should be invalid if it is less than 2 characters', () => {

    let usrnme = component.registerForm.controls.surname
    usrnme.setValue('M');
    expect(usrnme.errors).toBeTruthy();
  
  });


  it('surname should be valid if it is more than 2 characters', () => {

    let usrnme = component.registerForm.controls.surname
    usrnme.setValue('Mash');
    expect(usrnme.errors).toBeFalsy()
  
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


  it('form check - should check if form is valid or not if no values are entered', () => {

    expect(component.registerForm.valid).toBeFalsy();
  });

  it('form check - should check if form is valid or not if values are entered', () => {

    component.registerForm.controls.email.setValue('abc@gmail.com');
    component.registerForm.controls.password.setValue('01234567');

    expect(component.registerForm.valid).toBeFalsy();
    // expect(component.registerForm.valid).toBeFalsy();
  }); 
});
