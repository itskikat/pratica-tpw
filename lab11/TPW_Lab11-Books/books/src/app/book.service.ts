import { Injectable } from '@angular/core';
import { Book } from './book';
import { Observable } from 'rxjs/internal/Observable';
import { HttpClient, HttpHeaders } from '@angular/common/http'

const httpOptions = {
	headers: new HttpHeaders({'Content-Type': 'application/json'})
};

@Injectable({
	providedIn: 'root'
})

export class BookService {
	private baseURL = 'http://localhost:8000/ws/';

  	constructor(private http: HttpClient) { }

	getBookId(id: number): Observable<Book> {
		const url = this.baseURL + 'book?id=' + id;
		return this.http.get<Book>(url);
	}

	getBooks(): Observable<Book[]> {
		const url = this.baseURL + 'books';
		return this.http.get<Book[]>(url);
	}

	getBooksN(num: number): Observable<Book[]> {
		const url = this.baseURL + 'books?num=' + num;
		return this.http.get<Book[]>(url);
	}

	createBook(bo: Book): Observable<any> {
		const url = this.baseURL + 'bookcre';
		return this.http.post(url, bo, httpOptions);
	}

	updateBook(bo: Book): Observable<any> {
		const url = this.baseURL + 'bookupd';
		return this.http.put(url, bo, httpOptions);
	}

	deleteBook(bo: Book): Observable<any> {
		const url = this.baseURL + 'bookdel/' + bo.id;
		return this.http.delete<Book>(url, httpOptions);
	}
}
