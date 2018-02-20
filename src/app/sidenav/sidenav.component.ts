import {Component, OnDestroy, OnInit} from '@angular/core';
import {MediaMatcher} from '@angular/cdk/layout';
import {ChangeDetectorRef} from '@angular/core';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.css']
})
export class SidenavComponent implements OnInit {
  displayTable: any;
  constructor() {
  }
  ngOnInit () {
    this.displayTable = ['User', 'Bus', 'Trip', 'Subscriber', 'Plan', 'Route'];
  }
}
