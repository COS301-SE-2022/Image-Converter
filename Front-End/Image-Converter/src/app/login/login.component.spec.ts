import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Login } from '../classes/Login';
import { ConverterService } from '../shared/converter.service';

import { LoginComponent } from './login.component';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;
  let converterServiveSpy: jasmine.SpyObj<ConverterService>;

  beforeEach(async () => {
    const spy = jasmine.createSpyObj('ConverterService', ['login']);
    await TestBed.configureTestingModule({
      declarations: [ LoginComponent ],
      providers: [{provide: ConverterService, useValue: spy}]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    converterServiveSpy = TestBed.inject(ConverterService) as jasmine.SpyObj<ConverterService>;
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  it('#login should return stubbed value from a spy', () => {
    const stubValue = 'dummyValue';
    let stubAuthDetails:Login = {
      email : 'neo10@gmail.com',
      password : this.form.get('password')!.value
    } 
    converterServiveSpy.login.and.returnValue(stubValue);

  });
});
