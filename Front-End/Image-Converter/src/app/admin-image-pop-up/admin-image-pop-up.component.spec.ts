import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminImagePopUpComponent } from './admin-image-pop-up.component';

describe('AdminImagePopUpComponent', () => {
  let component: AdminImagePopUpComponent;
  let fixture: ComponentFixture<AdminImagePopUpComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminImagePopUpComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AdminImagePopUpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
