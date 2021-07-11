import React, { Component } from 'react';

class MyName extends Component {
    static defaultProps = {
        name: 'defalut'
    }
    render() {
        return (
            <div>
                My name is <b>{this.props.name}</b>.
            </div>
        );
    }
}

export default MyName;

