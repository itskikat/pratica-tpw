export class Publisher {
    id: number;
    name: string;
    city: string;
    country: string;
    website: string;
  
    constructor(id: number, name: string, city: string, country: string, website: string){
      this.id = id;
      this.name = name;
      this.city = city;
      this.country = country;
      this.website = website;
    }
  }