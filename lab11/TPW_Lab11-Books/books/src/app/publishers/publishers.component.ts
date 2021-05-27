import { Component, OnInit } from '@angular/core';
import { Publisher } from '../publisher';
import { PublisherService } from '../publisher.service';
import { PUBLISHERS } from '../publisherslist';

@Component({
  selector: 'app-publishers',
  templateUrl: './publishers.component.html',
  styleUrls: ['./publishers.component.css']
})
export class PublishersComponent implements OnInit {

  publishers!: Publisher[];

  constructor(private publisherService: PublisherService) { }

  ngOnInit(): void {
    this.getPublishers();
  }

  getPublishers(): void {
		this.publisherService.getPublishersN(4).subscribe(publishers => this.publishers = publishers);
	}

}
