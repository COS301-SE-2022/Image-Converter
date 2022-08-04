import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { MatDialog } from '@angular/material/dialog';
import { ImagePopupComponent } from './image-popup.component';

describe('ImagePopupComponent', () => {
  let component: ImagePopupComponent;
  let fixture: ComponentFixture<ImagePopupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ImagePopupComponent],
      imports: [MatDialog]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ImagePopupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
