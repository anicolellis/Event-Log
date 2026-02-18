import axios from 'axios';
import { useEffect, useState } from "react";
import BookForm from '../components/BookForm';

export function BookListPage() {
    const [books, setBooks] = useState([]);
    // Get book list when loading the page
    useEffect(() => {
        axios.get('http://localhost:8000/book')
            .then((response) => {
                setBooks(response.data);
            });
    }, []);

    return (
        <>
            <BookForm />
            <title>Alex's Book Log</title>
            <div>
                {books.map((book) => {
                    <div key={book.id}>
                        <div>
                            {`${book.title} by ${book.author}`}
                        </div>
                        <div>
                            {`Date finished: ${book.completion}`}
                        </div>
                    </div>
                })}
            </div>
        </>
    );
}