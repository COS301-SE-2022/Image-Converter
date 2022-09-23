import { ChangeDetectorRef, OnDestroy,Component, OnInit,ViewChild } from '@angular/core';
import {MediaMatcher} from '@angular/cdk/layout';
import { BreakpointObserver } from '@angular/cdk/layout';
import { MatSidenav } from '@angular/material/sidenav';
import { RouterModule } from '@angular/router';
import { Router } from '@angular/router';
import * as $ from 'jquery';


@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})

export class NavComponent implements OnInit {

  @ViewChild(MatSidenav)
 sidenav!: MatSidenav;

  mobileQuery: MediaQueryList;
  private _mobileQueryListener!: () => void;
  
  fillerNav = Array.from({length: 50}, (_, i) => `Nav Item ${i + 1}`);


  constructor(changeDetectorRef: ChangeDetectorRef, media: MediaMatcher,private observer: BreakpointObserver, private _router: Router) { 

    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListener = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addListener(this._mobileQueryListener);
  }

  ngOnInit(): void {
    
        $(document).ready(function () {
            $('#sidebarCollapse').on('click', function () {
                $('#sidebar').toggleClass('active');
            });
        });
    
  }

  ngAfterViewInit() {
    this.observer.observe(['(max-width: 800px)']).subscribe((res) => {
      if (res.matches) {
        this.sidenav.mode = 'over';
        this.sidenav.close();
      } else {
        this.sidenav.mode = 'side';
        this.sidenav.open();
      }
    });
  }
  ngOnDestroy(): void {
    this.mobileQuery.removeListener(this._mobileQueryListener);
  }
  
  onSubmitWelcome(){
    this._router.navigateByUrl('/welcome');
  }

  onSubmitLogin(){
    this._router.navigateByUrl('/login');
    // alert("button working");
  }

  onSubmitLanding(){
    this._router.navigateByUrl('/landing');
  }

}
