import React from 'react';
import Nav from 'react-bootstrap/Nav';
import { Link } from 'react-router-dom';

const Genre = (props) => (
    <Nav.Link as={Link} to={props.link}>
        {props.name}
    </Nav.Link>
);

export default Genre;