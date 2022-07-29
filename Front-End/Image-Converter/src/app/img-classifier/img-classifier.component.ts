// import { Component, OnInit } from '@angular/core';
// import { ConverterService } from '../shared/converter.service';
// // import { RestService } from './Services/rest.service';
// import { Weather } from '../classes/Weather';
// // import { Weather } from './Weather';

// @Component({
//   selector: 'app-img-classifier',
//   templateUrl: './img-classifier.component.html',
//   styleUrls: ['./img-classifier.component.scss']
// })


// export class ImgClassifierComponent implements OnInit {
//   title = 'AngularFlask';

//   constructor(private rs : ConverterService){}

//   headers = ["day","temperature", "windspeed",  "event"]

//   weather : Weather[] = [];

//   ngOnInit()
//   {

//     this.rs.readWeather().subscribe((result)  => {
//       // this.weather = result[0]["day"];
//       console.log(result[0]);
//       console.log("message coming through")
//     });
//   }

//   //   this.rs.readWeather().subscribe(
//   //     this.SubscribeService.assignValue().subscribe((result) => {
//   //       console.log(result);
//   //     });
      
//   //   )

//   //     this.rs.readWeather().subscribe
//   //       (
//   //         (response) => 
//   //         {
//   //           this.weather = response[0]["data"];
//   //         },
//   //         (error) =>
//   //         {
//   //           console.log("No Data Found" + error);
//   //         }

//   //       )
//   // }

//   // something.subscribe({
//   //   next: (user: User) =>  {
//   //     this.userProviderService.setUserId(user.userId);
//   //     this.proceed = true;
//   //   },
//   //   complete: () => {},
//   //   error: () => {}
//   // });

//   // readData()
//   // {
//   //   this.rs.readFile()
//   //   .subscribe
//   //       (
//   //         (response) => 
//   //         {
//   //           this.weather = response[0]["data"];
//   //         },
//   //         (error) =>
//   //         {
//   //           console.log("File doesn't exist..." + error);
//   //         }

//   //       )
//   // }

// }
