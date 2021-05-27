import { Component, OnInit, Input } from '@angular/core';
import { Author } from '../author';

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common'; 
import { AuthorService } from '../author.service';

@Component({
	selector: 'app-author-details',
	templateUrl: './author-details.component.html',
	styleUrls: ['./author-details.component.css']
})

export class AuthorDetailsComponent implements OnInit {

	author!: Author;

	constructor(
		private route: ActivatedRoute,
		private location: Location,
		private authorService: AuthorService  
	) { }

	ngOnInit(): void {
		this.getAuthor();
	}

	getAuthor(): void {
		const id = Number(this.route.snapshot.paramMap.get('id'));
		this.authorService.getAuthorId(id).subscribe(author => this.author = author);
	}

	update(): void {
		this.authorService.updateAuthor(this.author!).subscribe(() => this.goBack());
	}

	delete(): void {
		this.authorService.deleteAuthor(this.author!).subscribe(() => this.goBack());
	}

	goBack(): void {
		this.location.back();
	}

}
