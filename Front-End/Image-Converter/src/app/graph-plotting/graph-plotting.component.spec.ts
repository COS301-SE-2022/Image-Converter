import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GraphPlottingComponent } from './graph-plotting.component';

describe('GraphPlottingComponent', () => {
  let component: GraphPlottingComponent;
  let fixture: ComponentFixture<GraphPlottingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GraphPlottingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GraphPlottingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
