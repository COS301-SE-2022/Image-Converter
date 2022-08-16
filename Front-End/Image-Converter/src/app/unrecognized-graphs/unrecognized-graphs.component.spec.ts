import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UnrecognizedGraphsComponent } from './unrecognized-graphs.component';

describe('UnrecognizedGraphsComponent', () => {
  let component: UnrecognizedGraphsComponent;
  let fixture: ComponentFixture<UnrecognizedGraphsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UnrecognizedGraphsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UnrecognizedGraphsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
