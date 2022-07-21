import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImgClassifierComponent } from './img-classifier.component';

describe('ImgClassifierComponent', () => {
  let component: ImgClassifierComponent;
  let fixture: ComponentFixture<ImgClassifierComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ImgClassifierComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ImgClassifierComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
