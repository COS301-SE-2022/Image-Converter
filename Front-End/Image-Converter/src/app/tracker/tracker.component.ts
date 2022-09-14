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
  

  constructor(private trackerService: ConverterService) { }

  

  ngOnInit(): void {
    // Chart.registerables(...registerables);
    // const down = this.stats.incrementDownload();
    

    // const down  = JSON.parse(JSON.stringify(this.trackerService.activityTrackerGraphData()));
    // console.log(this.trackerService.activityTrackerGraphData());
    let responseData:any="";
    

    this.trackerService.activityTrackerGraphData().subscribe((data:any) => {
      responseData = JSON.parse(JSON.stringify(data));
      console.log(responseData.Uploads);


      const xlabels = ["Uploads","Downloads", "Unrecognised"];
    
    const ylabels = [responseData.Uploads, responseData.Downloads, responseData.Unrecognised];
    var myChart = new Chart("myChart", {
      type: 'bar',
      data: {
          labels: xlabels,
          datasets: [{
              label: 'Statistics of various actions performed', 
              data: ylabels,
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });
      
    });

    // console.log(down);

    
    
  }

}