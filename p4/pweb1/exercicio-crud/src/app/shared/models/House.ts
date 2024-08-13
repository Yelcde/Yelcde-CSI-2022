export class House {
  private static PRICE_PER_ROOM = 100;
  private static PRICE_PER_BATHROOM = 50;
  private static PRICE_PER_SQUARE_METER = 2;
  private static ID_AUTOINCREMENT = 0;
  private _id: number;
  private _dailyPrice: number;

  constructor(
    private _houseName: string,
    private _size: number,
    private _rooms: number,
    private _bathrooms: number
  ) {
    House.ID_AUTOINCREMENT += 1;
    this._id = House.ID_AUTOINCREMENT;

    const roomPrice = _rooms * House.PRICE_PER_ROOM;
    const bathroomPrice = _bathrooms * House.PRICE_PER_BATHROOM;
    const sizePrice = _size * House.PRICE_PER_SQUARE_METER;

    this._dailyPrice = Number((roomPrice + bathroomPrice + sizePrice).toFixed(2));
  }

  public get id(): number {
    return this._id;
  }

  public set id(v: number) {
    this._id = v;
  }

  public get houseName(): string {
    return this._houseName;
  }

  public get size(): number {
    return this._size;
  }

  public get rooms(): number {
    return this._rooms;
  }

  public get bathrooms(): number {
    return this._bathrooms;
  }

  public get dailyPrice(): number {
    return this._dailyPrice;
  }
}
