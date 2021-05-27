import { Component, OnInit } from '@angular/core';
import { Author } from '../author';
import { Publisher } from '../publisher';
import { Book } from '../book';
import { AuthorService } from '../author.service';
import { PublisherService } from '../publisher.service';
import { BookService } from '../book.service';

@Component({
	selector: 'app-overview',
	templateUrl: './overview.component.html',
	styleUrls: ['./overview.component.css']
})

export class OverviewComponent implements OnInit {

	authors!: Author[];
	publishers!: Publisher[];
	books!: Book[];

	constructor(private authorService: AuthorService, 
		private publisherService: PublisherService,
		private bookService: BookService
	) { }

	ngOnInit(): void {
		this.getAuthors();
		this.getPublishers();
		this.getBooks();
	}

	getAuthors(): void {
		this.authorService.getAuthorsN(4).subscribe(authors => this.authors = authors);
	}

	getPublishers(): void {
		this.publisherService.getPublishersN(4).subscribe(publishers => this.publishers = publishers);
	}

	getBooks(): void {
		this.bookService.getBooksN(4).subscribe(books => this.books = books);
	}

}
