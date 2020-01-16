import React, { Component } from 'react';

import './App.css';

const InitialState = {
  news: []
}

class  App extends Component {

  constructor() {
    super();
    this.state = {
      news: []
    }
  }
  componentDidMount(){
   
    fetch("http://192.168.99.100:6000/headlines")
        .then(results => results.json())
        .then(news => this.setState({news: news}));

  }

  // componentWillUnmount() {
  //   // Remember state for the next mount
  //   localStorage.setItem('newsState', JSON.stringify(this.state));
  // }

  render()
  
  {
    // this.state = localStorage.getItem("newsState") ? JSON.parse(localStorage.getItem("appState")) : InitialState;
  const news = this.state.news.map((n, index) => <li key = {index}>{n.title}</li>);
    console.log(this.state)
    return (
    <div>
      <ul>
       {news}
      </ul>

      
    </div>
  );
  }
}

export default App;
