import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthorsComponent } from './authors/authors.component';
import { OverviewComponent } from './overview/overview.component'; 
import { AuthorDetailsComponent } from './author-details/author-details.component';

import { PublishersComponent } from './publishers/publishers.component';
import { PublisherDetailsComponent } from './publisher-details/publisher-details.component';

import { BooksComponent } from './books/books.component';
import { BookDetailsComponent } from './book-details/book-details.component';


const routes: Routes = [
  {path: 'authors', component: AuthorsComponent}, 
  {path: 'overview', component: OverviewComponent}, 
  {path: 'authordetails/:num', component: AuthorDetailsComponent},

  {path: 'publishers', component: PublishersComponent}, 
  {path: 'publisherdetails/:num', component: PublisherDetailsComponent},

  {path: 'books', component: BooksComponent}, 
  {path: 'bookdetails/:num', component: BookDetailsComponent},
];

@NgModule({
  exports: [
    RouterModule
  ], 
  imports: [
    RouterModule.forRoot(routes)
  ]
})
export class AppRoutingModule { }
