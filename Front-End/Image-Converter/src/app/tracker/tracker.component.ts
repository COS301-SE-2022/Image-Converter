import { Component, OnInit } from '@angular/core';
import { Chart, registerables} from 'chart.js';
import {ConverterService} from './../shared/converter.service';
import {ComponentCommunicationService} from './../shared/component-communication.service';
import {ConversionComponent} from './../conversion/conversion.component';
// import { constants } from 'buffer';

Chart.register(...registerables);

@Component({
  selector: 'app-tracker',
  templateUrl: './tracker.component.html',
  styleUrls: ['./tracker.component.scss']
})



export class TrackerComponent implements OnInit {
  
  //used for loadig spinner
  loading=false;
  constructor(private trackerService: ConverterService) { }

  

  ngOnInit(): void {
    // Chart.registerables(...registerables);
    // const down = this.stats.incrementDownload();
    
    this.loading = true;
    // const down  = JSON.parse(JSON.stringify(this.trackerService.activityTrackerGraphData()));
    // console.log(this.trackerService.activityTrackerGraphData());
    let responseData:any="";
    

    this.trackerService.activityTrackerGraphData().subscribe((data:any) => {
      responseData = JSON.parse(JSON.stringify(data));
      console.log(responseData.Uploads);

      console.log(responseData.Downloads);
      console.log(responseData.Unrecognised);

      this.loading = false;

    const xlabels = ["Uploads","Downloads", "Unrecognised"];
    
    const ylabels = [responseData.Uploads, responseData.Downloads, responseData.Unrecognized];
    var myChart = new Chart("myChart", {
      type: 'bar',
      data: {
          labels: xlabels,
          datasets: [{
              label: 'Statistics of various actions performed', 
              data: ylabels,
              backgroundColor: [
                  'rgba(1, 41, 112,0.9)',
                  'rgb(47, 127, 231,0.9)',
                  'rgb(51, 51, 51,1)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  // 'rgba(255, 99, 132, 1)',
                  // 'rgba(54, 162, 235, 1)',
                  // 'rgba(255, 206, 86, 1)',
                  // 'rgba(75, 192, 192, 1)',
                  // 'rgba(153, 102, 255, 1)',
                  // 'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
        maintainAspectRatio: false,
          scales: {
              y: {
                ticks: { color: '#000000'}
              },
              x: {
                ticks: { color: '#000000'}
              }
          }
      }
  });
      
    });

    // console.log(down);

    
    
  }

}