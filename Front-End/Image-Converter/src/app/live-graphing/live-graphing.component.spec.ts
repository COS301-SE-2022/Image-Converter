import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LiveGraphingComponent } from './live-graphing.component';

describe('LiveGraphingComponent', () => {
  let component: LiveGraphingComponent;
  let fixture: ComponentFixture<LiveGraphingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LiveGraphingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LiveGraphingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
