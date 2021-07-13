import React, { Component } from 'react';
import icon from './assets/img/tshirt.svg'
import './assets/css/App.css';
import Location from './component/Location';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={icon} className="App" alt="icon" />
          <p>
            Today coordination
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
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
