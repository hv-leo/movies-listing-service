import React, { Component } from 'react';
import { HashRouter as Router } from 'react-router-dom';

import MoviesSite from './containers/MoviesSite/MoviesSite';

class App extends Component {
  render () {
    return (
      <Router>
        <MoviesSite />
      </Router>
    );
  }
}

export default App;
