import React, {useState} from 'react';
import { Route } from 'react-router-dom';
import { useAuth0 } from "@auth0/auth0-react";
import {
  NavItem,
  Button,
    NavbarBrand,
    NavbarToggler

} from "reactstrap";

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

const MoviesSite = (props) => {
    const {
    isAuthenticated,
    loginWithRedirect,
    logout,
        } = useAuth0();

    const [isOpen, setIsOpen] = useState(false);
    const toggle = () => setIsOpen(!isOpen);

    const logoutWithRedirect = () =>
    logout({
      returnTo: window.location.origin,
    });
    return (
        <div className="nav-container">
        <Container>
        <Navbar bg="light" variant="light" expand="lg">
            <NavbarBrand className="logo" />
            <NavbarToggler onClick={toggle} />
            <Nav className="d-none d-md-block" navbar>
                {!isAuthenticated && (
                    <NavItem>
                        <Button
                            id="qsLoginBtn"
                            color="primary"
                            className="btn-margin"
                            style={{ marginLeft: "auto" }}
                            onClick={() => loginWithRedirect()}
                        >
                            Log in
                        </Button>
                    </NavItem>
                )}
                {isAuthenticated && (<NavItem>
                        <Button
                            id="qsLoginBtn"
                            color="primary"
                            className="btn-margin"
                            style={{ marginLeft: "auto" }}
                            onClick={() => logoutWithRedirect()}
                        >
                            Log out
                        </Button>
                    </NavItem>)
                }
            </Nav>
            <Navbar.Brand href="/movies-feed/">MoviesFeed</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav"/>
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    {genres}
                </Nav>
            </Navbar.Collapse>
        </Navbar>
        <Route path={"/:genre"} component={MoviesFeed}/>
    </Container>
        </div>)
};

export default MoviesSite;