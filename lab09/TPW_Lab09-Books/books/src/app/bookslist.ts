import { AUTHORS } from './authorslist';
import { Book } from './book';
import { PUBLISHERS } from './publisherslist';

export const BOOKS: Book[] = [
    { num: 1, title: 'Will Grayson, Will Grayson', date: '06-04-2010', authors: [ AUTHORS[4] ], publishers: [ PUBLISHERS[2] ] },
    { num: 2, title: 'Livro do Desassossego', date: '1982', authors: [ AUTHORS[0] ], publishers: [ PUBLISHERS[4] ] },
    { num: 3, title: 'A Study in Scarlet', date: '1887', authors: [ AUTHORS[3] ], publishers: [ PUBLISHERS[1] ] },
    { num: 4, title: 'Fantastic Beasts and Where to Find Them', date: '03-2001', authors: [ AUTHORS[1] ], publishers: [ PUBLISHERS[0] ] },
    { num: 5, title: 'The Stand', date: '1978', authors: [ AUTHORS[2] ], publishers: [ PUBLISHERS[3] ] },
]
