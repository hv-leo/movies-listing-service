import React from 'react';
import { Route } from 'react-router-dom';
import Cookies from 'universal-cookie';

import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import InputGroup from 'react-bootstrap/InputGroup';
import FormControl from 'react-bootstrap/FormControl';
import Genre from '../../components/Genre/Genre';
import MoviesFeed from './MoviesFeed/NewsFeed';

const genresList = [
    { id: "comedy", name:"Comedy" },
    { id: "drama", name:"Drama" },
    { id: "romance", name:"Romance" },
    { id: "adventure", name:"Adventure" },
    { id: "horror", name:"Horror" },
    { id: "thriller", name:"Thriller" },
    { id: "sci-fi", name:"Sci-Fi" }
];

let genres = <p style={{ textAlign: 'center' }}>Something went wrong!</p>;
genres = genresList.map( genre => {
    const link = `/${genre.id}`;
    return (
        <Genre key={genre.name} name={genre.name} link={link} />
    );
} );

const MoviesSite = (props) => (
    <Container>
        <Navbar bg="light" variant="light" expand="lg">
            <Navbar.Brand href="/news-feed/">NewsFeed</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    {genres}
                </Nav>
            </Navbar.Collapse>
        </Navbar>
        <Route path={"/:genre"} component={MoviesFeed}/>
    </Container>
);

export default MoviesSite;