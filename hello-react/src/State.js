import React, { Component } from 'react';

class Counter extends Component{
    state = {
        number: 0
    }

    handleIncrese = () => {
        this.setState({
            number: this.state.number + 1
        });
    }

    handleDecrese = () => {
        this.setState({
            number: this.state.number - 1
        });
    }

    render() {
        return (
            <div>
                <h1>Counter</h1>
                <div>Value: {this.state.number}</div>
                <button onClick={this.handleIncrese}>+</button>
                <button onClick={this.handleDecrese}>-</button>
            </div>
        );
    }
}

export default Counter;
