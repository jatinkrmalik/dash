import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { BaseComponent } from './base/base.component';

import {
  MatButtonModule, MatCardModule, MatFormFieldModule, MatIconModule, MatInputModule, MatMenuModule, MatSidenavModule, MatTableModule,
  MatToolbarModule, MatTooltipModule, MatNavList
} from '@angular/material';
import { SidenavComponent } from './sidenav/sidenav.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { InfiniteScrollModule } from 'angular2-infinite-scroll';


const materialModules = [
  MatButtonModule,
  MatMenuModule,
  MatToolbarModule,
  MatIconModule,
  MatCardModule,
  MatSidenavModule,
  MatFormFieldModule,
  MatInputModule,
  MatTooltipModule,
];

@NgModule({
  declarations: [
    AppComponent,
    BaseComponent,
    SidenavComponent,

  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    MatTableModule,
    materialModules,
    InfiniteScrollModule,

  ],
  providers: [
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
