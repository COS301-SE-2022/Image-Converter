import { Component, OnInit } from '@angular/core';
import { Chart, registerables } from 'chart.js';

@Component({
  selector: 'app-graph-vis',
  templateUrl: './graph-vis.component.html',
  styleUrls: ['./graph-vis.component.scss']
})
export class GraphVisComponent implements OnInit  {
  title = 'angular-chart';
  constructor() {
    Chart.register(...registerables);
  }
  ngOnInit(): void {


          // 👇️ const input: HTMLInputElement | null

          // const value = input?.value;
          // console.log("A:  "+value) // 👉️ "Initial value"
    
          // if (input != null) {
          //   console.log("B:  "+input.value); // 👉️ "Initial value"
          // }
    
          // input?.addEventListener('input', function (event) {
          //   const target = event.target as HTMLInputElement;
          //   console.log("C:  "+target.value);
          // });



    // Line Chart
    // const lineCanvasEle: any = document.getElementById('line_chart')
    // const lineChar = new Chart(lineCanvasEle.getContext('2d'), {
    //   type: 'line',
    //     data: {
    //       labels: ['Test', 'February', 'March', 'April', 'May', 'June', 'July'],
    //       datasets: [
    //         { data: [12, 15, 18, 14, 11, 19, 12], label: 'Orders', borderColor: 'rgba(54, 162, 235)' },
    //         { data: [65, 59, 80, 81, 56, 55, 40], label: 'Sales', borderColor: 'rgb(75, 192, 192)' },
    //       ],
    //     },
    //     options: {
    //       responsive: true,
    //       scales: {
    //           y: {
    //               beginAtZero: true
    //           }
    //       }
    //     }
    //   });



    // Bar chart
    const barCanvasEle: any = document.getElementById('bar_chart')
    const input1 = document.getElementById('par1') as HTMLInputElement | null;

    input1?.addEventListener('input', function (event1) {
      const target1 = event1.target as HTMLInputElement;
      console.log("C:  "+target1.value);
    

    const barChart = new Chart(barCanvasEle.getContext('2d'), {
      type: 'bar',
        data: {
          labels: ['January', 'February', 'March', 'April'],
          datasets: [{
            label: 'Sales',
            data: [target1.value, 59, 80, 81],
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(255, 205, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
              'rgb(255, 99, 132)',
              'rgb(255, 159, 64)',
              'rgb(255, 205, 86)',
              'rgb(75, 192, 192)',
              'rgb(54, 162, 235)',
              'rgb(153, 102, 255)',
              'rgb(201, 203, 207)'
            ],
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          scales: {
              y: {
                  beginAtZero: false
              }
          }
        }

      });
      });
    


//       var bar_stacked = {
//     tooltips: {
//         enabled: false
//     },
//     scales: {
//         xAxes: [{
//             ticks: {
//                 beginAtZero:true,
//             },
//             stacked: true
//         }],
//         yAxes: [{
//             stacked: true
//         }]
//     },
//     legend:{
//         display:true      
//     }        
// };

// var ctx = document.getElementById("Chart1");
// var myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: ["Your graph"],
        
//          datasets: [{
//             data: [50000],
//             backgroundColor: "rgba(34,30,31,1)",
//            label: "Deductible"
//         },{
//             data: [250000],
//             backgroundColor: "rgba(243,125,33,1)",
//           label: "Protection"
//         },{
//             data: [50000],
//             backgroundColor: "rgba(0,150,145,1)",
//           label: "Additional Cost"
//         }]
//     },
//     options: bar_stacked,
// });

// //get input values
// function graphMe(){
  
//      var v1 = parseInt(document.getElementById("inputa").value);
//     var v2 = parseInt(document.getElementById("inputb").value);
//     var v3 = parseInt(document.getElementById("inputc").value);

//   if (!v1) { v1 = 0; }
//   if (!v2) { v2 = 0; }
//   if (!v3) { v3 = 0; }

// myChart.data.datasets[0].data[0] = v1
// myChart.data.datasets[1].data[0] = v2 - v1;
// myChart.data.datasets[2].data[0] = v3 - v2;
// myChart.update();  
//  }




  }
}