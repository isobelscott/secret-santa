import React, { Component } from 'react';


class PartyView extends Component {

    state = {
        partyId: 1,
        data: [],
        isLoading: false,
    };

    async loadPartyData() {
        this.setState({
            isLoading: true
        }, async () => {
            const url = `http://localhost:8000/api/parties?format=json&id=${this.state.partyID}`;
            const response = await fetch(url);
            const data = await response.json();
            this.setState({
                data: data[0],
                isLoading: false
            });
        });
    }

    partyDetails() {
        return (
            <div>
                <h1>{this.state.data.party_name}</h1>
                <div>
                    This party's draw is on {this.state.data.event_date}
                    &nbsp;and has a gift price max of ${this.state.data.gift_price_max}.
                    Contact your organizer, {this.state.data.organizer}, for assistance.
                </div>
                <div>
                    <h2>Your Party Members</h2>
                    Group ID: {this.state.data.group_id}
                </div>
            </div>
        )
    }

    partyBrowser() {

    }

    async componentDidMount() {
        await this.loadPartyData();
    }

    render() {
        return (
            <div>
                {this.partyDetails()}
            </div>
        );
    }
}

export default PartyView
