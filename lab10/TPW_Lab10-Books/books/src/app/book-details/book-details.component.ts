import { Component, OnInit, Input } from '@angular/core';
import { Book } from '../book';
import { BOOKS } from '../bookslist';

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common'; 

@Component({
	selector: 'app-book-details',
	templateUrl: './book-details.component.html',
	styleUrls: ['./book-details.component.css']
})
export class BookDetailsComponent implements OnInit {

	@Input() book?: Book;

	constructor(
		private route: ActivatedRoute,
		private location: Location  
	) { }

	ngOnInit(): void {
		this.getBook();
	}

	getBook(): void {
		const num = Number(this.route.snapshot.paramMap.get('num'));
		this.book = BOOKS.find(book => book.num === num);
	}

	goBack(): void {
		this.location.back();
	}

}
