import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { TotalCasosComponent } from './total-casos.component';

@NgModule({
  declarations: [TotalCasosComponent],
  imports: [
    CommonModule,
    HttpClientModule
  ],
  exports: [TotalCasosComponent] // Exporta o componente se necessário
})
export class TotalCasosModule { }
