import React from 'react';
import {useState} from 'react';
import Card from 'react-bootstrap/Card';
import { useAuth0 } from "@auth0/auth0-react";
import Nav from 'react-bootstrap/Nav';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart, faHeartBroken} from '@fortawesome/free-solid-svg-icons';

const Movies = (props) => {
    const { isAuthenticated } = useAuth0();
    const currentlyAFavorite = <FontAwesomeIcon icon={faHeart} />
    const notCurrentlyAFavorite = <FontAwesomeIcon icon={faHeartBroken}/>
    const [isActive, setIsActive] = useState(false);
    const handleClick = () => {
            setIsActive(current => !current);
    };
    const image = `${props.cover_image}` !== null ?
        <Card.Img variant="top" src={props.cover_image} alt="Image Unavailable" />
        : null;

    return (<Nav className="d-none d-md-block" navbar>
            {!isAuthenticated &&
                    <Card>
                        {image}
                        <Card.Body>
                            <Card.Title>{props.name}</Card.Title>
                        </Card.Body>
                    </Card>
            }
            {isAuthenticated &&
                    <Card>
                        {image}
                        <Card.Body>
                            <Card.Title>{props.name}</Card.Title>
                            <button
                                className="bi bi-suit-heart"
                                style={{float: 'right',
                                        backgroundColor: isActive ? 'red' : ''}}
                                onClick={handleClick}>
                                { isActive ? currentlyAFavorite : notCurrentlyAFavorite}
                             </button>
                        </Card.Body>
                    </Card>
            }
            </Nav>
    );
};

export default Movies;