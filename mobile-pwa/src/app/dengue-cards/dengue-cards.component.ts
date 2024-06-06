import { Component, OnInit } from '@angular/core';
import { DengueDataService } from '../dengue-data.service';

@Component({
  selector: 'app-dengue-cards',
  templateUrl: './dengue-cards.component.html',
  styleUrls: ['./dengue-cards.component.scss']
})
export class DengueCardsComponent implements OnInit {
  totalCases!: number; // Usa o operador "!" para indicar que será inicializado antes de ser usado
  totalDeaths!: number; // Usa o operador "!" para indicar que será inicializado antes de ser usado

  constructor(private dengueDataService: DengueDataService) { }

  ngOnInit(): void {
    this.totalCases = this.dengueDataService.getTotalCases();
    this.totalDeaths = this.dengueDataService.getTotalDeaths();
  }
}
