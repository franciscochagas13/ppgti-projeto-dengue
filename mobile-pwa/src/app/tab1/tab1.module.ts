import { IonicModule } from '@ionic/angular';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Tab1Page } from './tab1.page';
import { ExploreContainerComponentModule } from '../explore-container/explore-container.module';

import { Tab1PageRoutingModule } from './tab1-routing.module';
import { MapaParaibaComponentModule } from '../mapa-paraiba/mapa-paraiba.module';

import { LeafletModule } from '@asymmetrik/ngx-leaflet';
import { DengueCardsComponent } from '../dengue-cards/dengue-cards.component.spec';

@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    ExploreContainerComponentModule,
    MapaParaibaComponentModule,
    DengueCardsComponent,
    LeafletModule,
    Tab1PageRoutingModule
  ],
  declarations: [Tab1Page]
})
export class Tab1PageModule {}
