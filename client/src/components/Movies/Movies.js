import React from 'react';
import Card from 'react-bootstrap/Card';

const Movies = (props) => {
    const image = `${props.cover_image}` !== null ?
        <Card.Img variant="top" src={props.cover_image} alt="Image Unavailable" />
        : null;
    return (
        <Card>
            {image}
            <Card.Body>
                <Card.Title>{props.name}</Card.Title>
            </Card.Body>
        </Card>
    );
};

export default Movies;