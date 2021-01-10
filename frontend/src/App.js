import React, { Component } from 'react';
import './App.css';
import Person from "./components/Person";
import PartyView from "./components/Party";


class App extends Component {
  render() {
    return (
      <div>
        <PartyView/>
      </div>
    );
  }
}

export default App;
