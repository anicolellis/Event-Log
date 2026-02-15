import axios from "axios";
import { useState } from "react";

export default function BookForm() {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [release, setRelease] = useState('');
    const [completion, setCompletion] = useState('');

    function submitBook() {
        axios.post('http://localhost:8000/book', {
            title: title,
            author: author,
            release: release,
            completion: completion
        }).then((response) => {
            console.log(response.data);
        });
    }

    return (
        <form action={submitBook}>
            <label>
                Title:
                <input value = {title} onChange={e => setTitle(e.target.value)} />
            </label>
            <label>
                Author:
                <input value = {author} onChange={e => setAuthor(e.target.value)} />
            </label>
            <label>
                Release Date:
                <input type="date" value = {release} onChange={e => setRelease(e.target.value)} />
            </label>
            <label>
                Date Completed:
                <input type="date" value = {completion} onChange={e => setCompletion(e.target.value)} />
            </label>
            <button type="submit">Submit</button>
        </form>
    );
}