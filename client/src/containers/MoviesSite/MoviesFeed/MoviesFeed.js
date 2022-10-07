import React, { useState, useEffect } from 'react';
import { useAuth0 } from "@auth0/auth0-react";
import CardColumns from 'react-bootstrap/CardColumns';
import Movies from '../../../components/Movies/Movies';


export const MoviesFeed = (props) => {
    const {getAccessTokenSilently,  isAuthenticated } = useAuth0();
    const [movies, setMovies] = useState( [] );
    const [moviesFeed, setMoviesFeed] = useState();
    const [error, setError] = useState( true );
    const [errorMessage, setErrorMessage] = useState();

    useEffect( () => {
        ( async () => {
            const genre = await props.match.params.genre;
            // Offline strategy.
            if (!navigator.onLine && localStorage.getItem(genre) !== null) {
                setError(false);
                setMovies(JSON.parse(localStorage.getItem(genre)));
            }
            else if (!isAuthenticated){
                setErrorMessage("Please log in first.")
            }
            else {
                const token = await getAccessTokenSilently();
                await fetch(`http://localhost/server/movies/${genre}`, {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }).then(
                        response => {
                            console.log(response.status)
                            return response.json()
                        }
                    ).then(
                        movies => {
                        setError(false);
                        setMovies(movies);
                        localStorage.setItem(genre, JSON.stringify(movies));
                    }).catch(error => {
                        setError(true);
                        setErrorMessage(error.message);
                    });
            }
        }) ();
    }, [ props.match.params.genre, getAccessTokenSilently,  isAuthenticated, errorMessage] );

    useEffect( () => {
        ( async () => {
            let moviesFeed = <p style={{textAlign: 'center'}}>{errorMessage}</p>;
            if (!error) {
                moviesFeed = movies?.map(movie => {
                    return (
                        <Movies
                            cover_image={movie.cover_image}
                            name={movie.name}
                        />
                    );
                });
            }
            setMoviesFeed(moviesFeed);
            })();
    }, [ movies, error, errorMessage ] );

    return (
        <CardColumns>
            {moviesFeed}
        </CardColumns>
    );
};

export default MoviesFeed;