import { Author } from "./author";
import { Publisher } from "./publisher";

export class Book {
    id: number;
    title: string;
    date: string;
    authors: Author[];
    publishers: Publisher[];
  
    constructor(id: number, title: string, date: string, authors: Author[], publishers: Publisher[]) {
      this.id = id;
      this.title = title;
      this.date = date;
      this.authors = authors;
      this.publishers = publishers;
    }
  }