import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './/app-routing.module';
import { AuthorsComponent } from './authors/authors.component';
import { PublishersComponent } from './publishers/publishers.component';
import { BooksComponent } from './books/books.component';
import { OverviewComponent } from './overview/overview.component';
import { AuthorDetailsComponent } from './author-details/author-details.component';
import { PublisherDetailsComponent } from './publisher-details/publisher-details.component';
import { BookDetailsComponent } from './book-details/book-details.component';

@NgModule({
  declarations: [
    AppComponent,
    AuthorsComponent,
    PublishersComponent,
    BooksComponent,
    OverviewComponent,
    AuthorDetailsComponent,
    PublisherDetailsComponent,
    BookDetailsComponent
  ],
  imports: [
    BrowserModule,
    FormsModule, 
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
