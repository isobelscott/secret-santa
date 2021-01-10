import React, { Component } from 'react';

class Person extends Component {
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
                data: data,
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
                {this.state.data.map((data, key) => {
                  return (
                    <div key={key}>
                      {data.id +
                        " , " +
                        data.first_name +
                        " ," +
                        data.email +
                        ", " +
                        data.exclusions}
                    </div>
                  );
                })}
            </div>
        );
    }
}

export default Person