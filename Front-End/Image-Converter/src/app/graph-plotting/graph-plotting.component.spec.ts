// import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HttpClientTestingModule } from "@angular/common/http/testing";
import { ComponentFixture, TestBed } from "@angular/core/testing";
import { ReactiveFormsModule, FormsModule } from "@angular/forms";
import { RouterTestingModule } from "@angular/router/testing";
import { ConverterService } from "../shared/converter.service";
import { GraphPlottingComponent } from "./graph-plotting.component";


describe('Testing GraphPlottingComponent', () => {
  let component: GraphPlottingComponent;
  let fixture: ComponentFixture<GraphPlottingComponent>;
  let service: ConverterService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule,
        RouterTestingModule
      ],
      declarations: [ GraphPlottingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GraphPlottingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();


    service = TestBed.inject(ConverterService);

  });


  it('Should create a component', () => {
    expect(component).toBeTruthy();
  });

  it('Form is invalid when empty', () => {
    expect(component.form.valid).toBeFalsy();
    });
  

    // it('Testing onSubmitFunction', () => {

      // const mockFormula={formula: "x+12"}
      // const mockResponse = {image: "https://storage.googleapis.com/hardcode-9aba7.appspot.com/148Converted.jpg?Expires=1691423520&GoogleAccessId=firebase-adminsdk-fdx52%40hardcode-9aba7.iam.gserviceaccount.com&Signature=hzmJ6vtsNbJOuuis0cXdOuSKESDIakTZ33XmSo%2Flte0GPGcGZkQHBSVXZXd3ZffsYG9PNw5bEp2DVMwSdSxo5AHh0m%2Fz64qAF84KdAT2rCDfcjngzEiz8G%2BAMuHFhy6bs2Qztbj0SRqjBBrHoQAv1q8NT%2B5Wbr1L2DVXOcWpIIFyEC1Vi8VfkMmdyFvV5gqrRLOEanyANUPkDeLrUTpiS1zbNnLT4o4Q8M0FlMIOiQesZqHEMzsTURr1HvyKs9koFLH3YD3y7%2F%2B7i1JM8RYrZSIYt8JgB9zbI598T%2BCChHkBoBNbJEmjVT41zMwrjxX625qf0GcghW4YKynRrQpDTQ%3D%3D"}

      
      
      // service.postFormula(mockFormula).subscribe(resultData => 
      //   {
      //     const result = JSON.parse(JSON.stringify(resultData));
      //     expect(result.image).toEqual(mockResponse);

      //   });




    it('Testing onSubmitFunction()',
    (done: DoneFn) => {
             const mockFormula={formula: "x+12"}
          const mockResponse = {image: "https://storage.googleapis.com/hardcode-9aba7.appspot.com/148Converted.jpg?Expires=1691423520&GoogleAccessId=firebase-adminsdk-fdx52%40hardcode-9aba7.iam.gserviceaccount.com&Signature=hzmJ6vtsNbJOuuis0cXdOuSKESDIakTZ33XmSo%2Flte0GPGcGZkQHBSVXZXd3ZffsYG9PNw5bEp2DVMwSdSxo5AHh0m%2Fz64qAF84KdAT2rCDfcjngzEiz8G%2BAMuHFhy6bs2Qztbj0SRqjBBrHoQAv1q8NT%2B5Wbr1L2DVXOcWpIIFyEC1Vi8VfkMmdyFvV5gqrRLOEanyANUPkDeLrUTpiS1zbNnLT4o4Q8M0FlMIOiQesZqHEMzsTURr1HvyKs9koFLH3YD3y7%2F%2B7i1JM8RYrZSIYt8JgB9zbI598T%2BCChHkBoBNbJEmjVT41zMwrjxX625qf0GcghW4YKynRrQpDTQ%3D%3D"}
    

          service.postFormula(mockFormula).subscribe(resultData => 
            {
              const result = JSON.parse(JSON.stringify(resultData));
              expect(result.image).toEqual(mockResponse);
    
            });
            done();
          });
    



//Download Function

  //   it("should make XHR request", () =>  {

  //     // setup
  //      var xhr = {
  //          send: jasmine.createSpy('send'),
  //          open: jasmine.createSpy('open')
  //      };
  //      XMLHttpRequest = jasmine.createSpy('XMLHttpRequest');
  //      XMLHttpRequest.and.callFake(component.downloadFile("image") {
  //          return xhr;
  //      });

   
  //      // act
   
  //      component.downloadFile("h").onload;
   
  //      // assert
   
  //      expect(xhr.send).toHaveBeenCalled(); 

  //  });


});


