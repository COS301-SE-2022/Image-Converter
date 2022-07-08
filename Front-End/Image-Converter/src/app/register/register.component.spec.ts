import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterComponent } from './register.component';

describe('RegisterComponent', () => {
  let component: RegisterComponent;
  let fixture: ComponentFixture<RegisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegisterComponent ]
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

  
  it("hide attribute", () => {
    expect(component.hide).toBe(true);
  });

  it("match attribute", () => {
    expect(component._match).toBe(boolean);
  });

  it("button attribute", () => {
    expect(component.buttonLogin).toBeTruthy("");
  });

  it("submitted status attribute", () => {
    expect(component.submitted).toBe(false);
  });

  it("title attribute", () => {
    expect(component.title).toBe("reactiveformproject");
  });


  it("get name function", () => {
    expect(component.name()).toBe("name");
  });

  it("get password function ", () => {
    expect(component.password()).toBe("password");
  });

  it("get surname function ", () => {
    expect(component.surname()).toBe("surname");
  });

  it("get email function ", () => {
    expect(component.email()).toBe("email");
  });

  it("get cpassword function ", () => {
    expect(component.confirmPassword()).toBe("cpassword");
  });

});
