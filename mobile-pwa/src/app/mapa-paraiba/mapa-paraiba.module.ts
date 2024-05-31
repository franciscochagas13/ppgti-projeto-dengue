import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';
import { MapaParaibaComponent } from './mapa-paraiba.component';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [ CommonModule, FormsModule, IonicModule,LeafletModule,HttpClientModule],
  declarations: [MapaParaibaComponent],
  exports: [MapaParaibaComponent]
})
export class MapaParaibaComponentModule {}
