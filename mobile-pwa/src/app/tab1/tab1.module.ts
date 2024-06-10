import { IonicModule } from '@ionic/angular';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Tab1Page } from './tab1.page';
import { ExploreContainerComponentModule } from '../explore-container/explore-container.module';
import { Tab1PageRoutingModule } from './tab1-routing.module';
import { MapaParaibaComponentModule } from '../mapa-paraiba/mapa-paraiba.module';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';
import { TotalCasosModule } from '../total-casos/total-casos.module'; // Importe o módulo TotalCasosModule

@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    ExploreContainerComponentModule,
    MapaParaibaComponentModule,
    LeafletModule,
    Tab1PageRoutingModule,
    TotalCasosModule // Importe aqui se estiver usando diretamente
  ],
  declarations: [Tab1Page],
  schemas: [CUSTOM_ELEMENTS_SCHEMA] // Adicione o CUSTOM_ELEMENTS_SCHEMA se necessário
})
export class Tab1PageModule {}
