import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AppComponent } from './app.component';

describe('AppComponent', () => {
  let component: AppComponent;
  let fixture: ComponentFixture<AppComponent>;

  beforeEach(async() => {
    TestBed.configureTestingModule({
      declarations: [AppComponent]
    }).compileComponents();
    
    fixture = TestBed.createComponent(AppComponent);
    component = fixture.componentInstance;
  });

  it('should be defined at this point', () => {
    expect(component).toBeDefined();
  });
});