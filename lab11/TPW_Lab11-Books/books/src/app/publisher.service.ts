import { Injectable } from '@angular/core';
import { Publisher } from './publisher';
import { Observable } from 'rxjs/internal/Observable';
import { HttpClient, HttpHeaders } from '@angular/common/http'

const httpOptions = {
	headers: new HttpHeaders({'Content-Type': 'application/json'})
};

@Injectable({
	providedIn: 'root'
})

export class PublisherService {
	private baseURL = 'http://localhost:8000/ws/';

  	constructor(private http: HttpClient) { }

	getPublisherId(id: number): Observable<Publisher> {
		const url = this.baseURL + 'publisher?id=' + id;
		return this.http.get<Publisher>(url);
	}

	getPublishers(): Observable<Publisher[]> {
		const url = this.baseURL + 'publishers';
		return this.http.get<Publisher[]>(url);
	}

	getPublishersN(num: number): Observable<Publisher[]> {
		const url = this.baseURL + 'publishers?num=' + num;
		return this.http.get<Publisher[]>(url);
	}

	createPublisher(pu: Publisher): Observable<any> {
		const url = this.baseURL + 'publishercre';
		return this.http.post(url, pu, httpOptions);
	}

	updatePublisher(pu: Publisher): Observable<any> {
		const url = this.baseURL + 'publisherupd';
		return this.http.put(url, pu, httpOptions);
	}

	deletePublisher(pu: Publisher): Observable<any> {
		const url = this.baseURL + 'publisherdel/' + pu.id;
		return this.http.delete<Publisher>(url, httpOptions);
	}
}
