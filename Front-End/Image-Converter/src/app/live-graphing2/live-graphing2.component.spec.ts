import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LiveGraphing2Component } from './live-graphing2.component';

describe('LiveGraphing2Component', () => {
  let component: LiveGraphing2Component;
  let fixture: ComponentFixture<LiveGraphing2Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LiveGraphing2Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LiveGraphing2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
