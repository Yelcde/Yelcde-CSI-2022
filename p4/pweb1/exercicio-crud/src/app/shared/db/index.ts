import { House } from '../models/House';

export class DB {
  private static houses: House[] = [
    new House('Villa', 250, 4, 3),
    new House('Cottage', 180, 3, 2),
    new House('Mansion', 500, 8, 5),
    new House('Apartment', 120, 2, 1),
    new House('Townhouse', 200, 5, 3)
  ];

  public static addHouse(house: House): void {
    DB.houses.push(house);
  }

  public static removeHouse(id: number): void {
    DB.houses = DB.houses.filter(house => house.id !== id);
  }

  public static updateHouse(house: House): void {
    DB.houses = DB.houses.map(data => {
      if (data.id === house.id) return house;

      return data;
    });
  }

  public static getHouses(): House[] {
    return DB.houses;
  }

  public static getHouse(id: number): House {
    const house = DB.houses.filter(house => house.id === id)[0];
    return house;
  }
}
