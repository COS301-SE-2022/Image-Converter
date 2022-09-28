import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ComponentCommunicationService } from '../shared/component-communication.service';


import { FilterComponent } from './filter.component';

describe('FilterComponent', () => {
  let component: FilterComponent;
  let fixture: ComponentFixture<FilterComponent>;
  let communication: ComponentCommunicationService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FilterComponent ],
      providers: [ComponentCommunicationService]
    }).compileComponents();

    fixture = TestBed.createComponent(FilterComponent);
    component = fixture.componentInstance;
    communication = TestBed.inject(ComponentCommunicationService);
    fixture.detectChanges();
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  describe('testing the deaulft attribute values of this component', () => {
    it('should be false', () => {
      expect(component.dispBool).toBeFalse();
    });
  
    it('should be equal = \'default message\'', () => {
      expect(component.message).toBe('default message');
    });

    it('should be defined', () => {
      expect(component.subscription).toBeDefined();
    });

    
  });

  it('')
});



