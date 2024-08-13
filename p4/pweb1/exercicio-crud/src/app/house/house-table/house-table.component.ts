import { Component } from '@angular/core';

import { DB } from '../../shared/db';

@Component({
  selector: 'app-house-table',
  templateUrl: './house-table.component.html',
  styleUrl: './house-table.component.css'
})
export class HouseTableComponent {
  dataSource = DB.getHouses();
  displayedColumns: string[] = ['houseName', 'size', 'rooms', 'bathrooms', 'dailyPrice', 'actions'];

  public deleteHouse(id: number): void {
    DB.removeHouse(id);
    this.dataSource = DB.getHouses();
  }
}
