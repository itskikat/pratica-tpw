import { Component, OnInit, Input } from '@angular/core';
import { Publisher } from '../publisher';
import { PUBLISHERS } from '../publisherslist';

import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common'; 
import { PublisherService } from '../publisher.service';

@Component({
	selector: 'app-publisher-details',
	templateUrl: './publisher-details.component.html',
	styleUrls: ['./publisher-details.component.css']
})
export class PublisherDetailsComponent implements OnInit {

	publisher!: Publisher;

	constructor(
		private route: ActivatedRoute,
		private location: Location,
		private publisherService: PublisherService  
	) { }

	ngOnInit(): void {
		this.getPublisher();
	}

	getPublisher(): void {
		const id = Number(this.route.snapshot.paramMap.get('id'));
		console.log(id);
		this.publisherService.getPublisherId(id).subscribe(publisher => this.publisher = publisher);
	}

	update(): void {
		this.publisherService.updatePublisher(this.publisher!).subscribe(() => this.goBack());
	}

	delete(): void {
		this.publisherService.deletePublisher(this.publisher!).subscribe(() => this.goBack());
	}

	goBack(): void {
		this.location.back();
	}

}
