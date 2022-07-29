import { TestBed } from '@angular/core/testing';
import { ConverterService } from './converter.service';
import { HttpClientTestingModule,
         HttpTestingController } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { HttpRequest } from '@angular/common/http';

describe('Testing HTTP requests of Converter Component', () => {
  // We declare the variables that we'll use for the Test Controller and for our Service
  let httpMock: HttpTestingController;
  let service: ConverterService;
  

    beforeEach((() => {
      TestBed.configureTestingModule({
        imports: [
          HttpClientTestingModule,
          RouterTestingModule
        ]
      });
  
      service = TestBed.inject(ConverterService);
      httpMock = TestBed.inject(HttpTestingController);
    }));

    it('Component should be created', () => {
      expect(service).toBeTruthy();
    });

    it('Testing login', () => {

        const MockLogin={ email:"testEmail@gmail.com", password:"testPassword"}

        service.login(MockLogin).subscribe(result => 
            {
                expect(result).toBeTruthy();
            });


        const req = httpMock.expectOne( (req: HttpRequest<any>)  => req.urlWithParams == "http://localhost:5000/login");
        expect(req.request.method).toBe('POST');
        expect(req.request.url).toEqual('http://localhost:5000/login');

        req.flush({});
        httpMock.verify();

      });


      it('Testing register', () => {

        const MockRegister={ name: "Test", surname: "Test", email:"testEmail@gmail.com", password:"testPassword", cpassword: "testPassword"}

        service.register(MockRegister).subscribe(result => 
            {
                expect(result).toBeTruthy();
            });


        const req = httpMock.expectOne( (req: HttpRequest<any>)  => req.urlWithParams == "http://localhost:5000/register");
        expect(req.request.method).toBe('POST');
        expect(req.request.url).toEqual('http://localhost:5000/register');

        req.flush({});
        httpMock.verify();

      });



      it('Testing post image', () => {

        service.postImg("post image").subscribe(result => 
            {
                expect(result).toBeTruthy();
            });


        const req = httpMock.expectOne( (req: HttpRequest<any>)  => req.urlWithParams == "http://localhost:5000/picture");
        expect(req.request.method).toBe('POST');
        expect(req.request.url).toEqual('http://localhost:5000/picture');

        req.flush({});
        httpMock.verify();


      });




    it('Testing Upload History', () => {

        service.getUploadHistory().subscribe(result => 
            {
                expect(result).toBeTruthy();
            });


        const req = httpMock.expectOne( (req: HttpRequest<any>)  => req.urlWithParams == "http://localhost:5000/uploadhistory");
        expect(req.request.method).toBe('GET');
        expect(req.request.url).toEqual('http://localhost:5000/uploadhistory');

        req.flush({});
        httpMock.verify();


      });


      it('Testing delete image', () => {

        service.deleteImage("pic").subscribe(result => 
            {
                expect(result).toBeTruthy();
            });


        const req = httpMock.expectOne( (req: HttpRequest<any>)  => req.urlWithParams == "http://localhost:5000/deletehistory");
        expect(req.request.method).toBe('POST');
        expect(req.request.url).toEqual('http://localhost:5000/deletehistory');

        req.flush({});
        httpMock.verify();


      });

      
 
});


















