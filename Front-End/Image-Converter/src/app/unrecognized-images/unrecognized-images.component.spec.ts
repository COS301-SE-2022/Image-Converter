import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UnrecognizedImagesComponent } from './unrecognized-images.component';

describe('UnrecognizedImagesComponent', () => {
  let component: UnrecognizedImagesComponent;
  let fixture: ComponentFixture<UnrecognizedImagesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UnrecognizedImagesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UnrecognizedImagesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
