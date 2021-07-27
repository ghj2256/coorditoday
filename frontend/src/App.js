import React, { Component } from 'react';
import icon from './assets/img/tshirt.svg'
import './assets/css/App.css';
import Header from './component/Header';
import Weather from './component/Weather'
import Button from '@material-ui/core/Button' 

class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <div className="App-contents">
          <p><Weather /></p>
          <img src={icon} className="App-img" alt="icon" />
          <p>
            Today coordination
          </p>
          <a
            className="App-link"
            href="https://www.weather.go.kr"
            target="_blank"
            rel="noopener noreferrer"
          >
            Weather Information
          </a>
          <p>
            <Button variant="contained" color="primary">
              Hello World
            </Button>
          </p>
        </div>
      </div>
    );
  }
}

export default App;
