import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginComponent } from './login.component';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoginComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });



  it("hide attribute", () => {
    expect(component.hide).toBe(true);
  });

  it("match attribute", () => {
    expect(component._match).toBe(true);
  });

  it("button attribute", () => {
    expect(component.buttonLogin).toBeTruthy("");
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });


  // it("get username function", () => {
  //   expect(component.username).toBe("username");
  // });

  // it("get password function ", () => {
  //   expect(component.password).toBe("password");
  // });
});
