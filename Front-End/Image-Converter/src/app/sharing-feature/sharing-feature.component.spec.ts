import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SharingFeatureComponent } from './sharing-feature.component';

describe('SharingFeatureComponent', () => {
  let component: SharingFeatureComponent;
  let fixture: ComponentFixture<SharingFeatureComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SharingFeatureComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SharingFeatureComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
