import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GraphingInputComponent } from './graphing-input.component';

describe('GraphingInputComponent', () => {
  let component: GraphingInputComponent;
  let fixture: ComponentFixture<GraphingInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GraphingInputComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GraphingInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
