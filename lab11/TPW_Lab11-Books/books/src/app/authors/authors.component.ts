import { Component, OnInit } from '@angular/core';
import { Author } from '../author';
import { AuthorService } from '../author.service';
import { AUTHORS } from '../authorslist';

@Component({
  selector: 'app-authors',
  templateUrl: './authors.component.html',
  styleUrls: ['./authors.component.css']
})
export class AuthorsComponent implements OnInit {

  authors?: Author[];
  selectedAuthor!: Author;

  constructor(private authorService: AuthorService) {  }

  onSelect(author: Author): void {
    this.selectedAuthor = author;
  }

  ngOnInit(): void {
    this.getAuthors();
  }

  getAuthors(): void {
    this.authorService.getAuthors().subscribe(authors => this.authors = authors);
  }

}
