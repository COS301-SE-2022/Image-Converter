import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-payfast',
  templateUrl: './payfast.component.html',
  styleUrls: ['./payfast.component.scss']
})
export class PayfastComponent implements OnInit {
  // url ="https://sandbox.payfast.co.za/eng/process ";
  url = "https://www.payfast.co.za/eng/process";
  constructor() { }

  ngOnInit(): void {
  }

}
