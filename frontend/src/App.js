import React, { Component } from 'react';
import icon from './assets/img/tshirt.svg'
import './assets/css/App.css';
import Search from './component/Search';
import Weather from './component/Weather'
import Button from '@material-ui/core/Button' 

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <p>오늘 뭐입지?</p>
        </header>
        <p><Search /></p>
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
          <Button variant="contained" color="primary">
            Hello World
          </Button>
        </div>
      </div>
    );
  }
}

export default App;
