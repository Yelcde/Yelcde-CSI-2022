import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

import { DB } from '../../shared/db';
import { House } from '../../shared/models/House';

@Component({
  selector: 'app-house-form',
  templateUrl: './house-form.component.html',
  styleUrl: './house-form.component.css'
})
export class HouseFormComponent {
  public id: number = 0;
  public houseName: string = ''
  public size: string = ''
  public rooms: string = ''
  public bathrooms: string = ''

  constructor(private _snackBar: MatSnackBar, private _route: ActivatedRoute) {}

  ngOnInit() {
    this.id = Number(this._route.snapshot.paramMap.get('id'));

    if (this.id !== 0) {
      const house = DB.getHouse(this.id);
      this.houseName = house.houseName;
      this.size = house.size.toString();
      this.rooms = house.rooms.toString();
      this.bathrooms = house.bathrooms.toString();
    }
  }

  public registerNewHouse(): void {
    const newHouse = new House(
      this.houseName,
      Number(this.size),
      Number(this.rooms),
      Number(this.bathrooms)
    )

    DB.addHouse(newHouse);

    this.clearInputs();
    this.openSnackBar('Casa cadastrada com sucesso!');
  }

  public editHouse(): void {
    const house = new House(
      this.houseName,
      Number(this.size),
      Number(this.rooms),
      Number(this.bathrooms)
    );

    house.id = this.id;

    DB.updateHouse(house);
    this.clearInputs();
    this.openSnackBar('Casa editada com sucesso!');
  }

  private openSnackBar(message: string): void {
    this._snackBar.open(message, 'Ok', {
      duration: 3000
    });
  }

  private clearInputs(): void {
    this.houseName = '';
    this.size = '';
    this.rooms = '';
    this.bathrooms = '';
  }
}
