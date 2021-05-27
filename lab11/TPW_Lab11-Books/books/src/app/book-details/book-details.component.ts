import { Component, OnInit, Input } from '@angular/core';
import { Book } from '../book';

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common'; 
import { BookService } from '../book.service';

@Component({
	selector: 'app-book-details',
	templateUrl: './book-details.component.html',
	styleUrls: ['./book-details.component.css']
})
export class BookDetailsComponent implements OnInit {

	book!: Book;

	constructor(
		private route: ActivatedRoute,
		private location: Location,
		private bookService: BookService  
	) { }

	ngOnInit(): void {
		this.getBook();
	}

	getBook(): void {
		const id = Number(this.route.snapshot.paramMap.get('id'));
		this.bookService.getBookId(id).subscribe(book => this.book = book);
	}

	update(): void {
		this.bookService.updateBook(this.book!).subscribe(() => this.goBack());
	}

	delete(): void {
		this.bookService.deleteBook(this.book!).subscribe(() => this.goBack());
	}

	goBack(): void {
		this.location.back();
	}

}
