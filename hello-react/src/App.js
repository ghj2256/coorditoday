import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MyName from './MyName';
import Counter from './State';

class App extends Component {
  render(){
    const style = {
      backgroundColor: 'black',
      padding: '16px',
      color: 'white',
      fontSize: '12px'
    };
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
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
        <div style={style}>
          {
            1 + 1 === 2 && (<div>right!</div>)
          }
          <MyName  />
        </div>
        <div>
          <Counter />
        </div>
      </div>
    );
  }
}

export default App;
