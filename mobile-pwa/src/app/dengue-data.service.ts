import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DengueDataService {
  private totalCases: number = 1234; // Exemplo de número de casos de dengue
  private totalDeaths: number = 56;  // Exemplo de número de óbitos por dengue

  constructor() { }

  getTotalCases(): number {
    return this.totalCases;
  }

  getTotalDeaths(): number {
    return this.totalDeaths;
  }
}
