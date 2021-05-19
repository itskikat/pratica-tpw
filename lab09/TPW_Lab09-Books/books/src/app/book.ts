import { Author } from "./author";
import { Publisher } from "./publisher";

export class Book {
    num: number;
    title: string;
    date: string;
    authors: Author[];
    publishers: Publisher[];
  
    constructor(num: number, title: string, date: string, authors: Author[], publishers: Publisher[]) {
      this.num = num;
      this.title = title;
      this.date = date;
      this.authors = authors;
      this.publishers = publishers;
    }
  }