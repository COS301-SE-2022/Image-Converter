import { Component, OnInit, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  enterText: string='';

  @Output()
  searchText: EventEmitter<string> = new EventEmitter<string>();

  onSearch(){
    this.searchText.emit(this.enterText);
  }
}
