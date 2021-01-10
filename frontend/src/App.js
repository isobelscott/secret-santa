import React, { Component } from 'react';
import './App.css';

class Persons extends Component {
    state = {
        data: [],
        isLoading: false,
    };
    async loadData() {
        this.setState({
            isLoading: true
        }, async () => {
            const url = `http://localhost:8000/api/persons?format=json`;
            const response = await fetch(url);
            const data = await response.json();
            this.setState({
                data: data.results,
                isLoading: false
            });
        });
    }
    async componentDidMount() {
        await this.loadData();
    }
    render() {
        return (
            <div>
                {this.state.data}
            </div>
        );
    }
}



class App extends Component {
  render() {
    return (
      <div>
        <Persons/>
      </div>
    );
  }
}

export default App;
