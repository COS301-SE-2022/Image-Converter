import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TemplateMatchingComponent } from './template-matching.component';

describe('TemplateMatchingComponent', () => {
  let component: TemplateMatchingComponent;
  let fixture: ComponentFixture<TemplateMatchingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TemplateMatchingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TemplateMatchingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
