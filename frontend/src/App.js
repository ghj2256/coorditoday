import React, { Component } from 'react';
import icon from './assets/img/tshirt.svg'
import './assets/css/App.css';
import Location from './component/Location';
import Search from './component/Search';
import Weather from './component/Weather'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <p><Search /></p>
          <p><Weather /></p>
          <img src={icon} className="App-logo" alt="icon" />
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
        </header>
        <div>
          <Location />
        </div>
      </div>
    );
  }
}

export default App;
