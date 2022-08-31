import React from 'react';
import { Route } from 'react-router-dom';
import Cookies from 'universal-cookie';

import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Genre from '../../components/Genre/Genre';
import MoviesFeed from './MoviesFeed/MoviesFeed';

const genresList = [
    { id: "Comedy", name:"Comedy" },
    { id: "Drama", name:"Drama" },
    { id: "Romance", name:"Romance" },
    { id: "Adventure", name:"Adventure" },
    { id: "Horror", name:"Horror" },
    { id: "Thriller", name:"Thriller" },
    { id: "Sci-Fi", name:"Sci-Fi" }
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
            <Navbar.Brand href="/movies-feed/">MoviesFeed</Navbar.Brand>
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