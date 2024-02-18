import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Header from './components/Header';
import 'bootstrap/dist/css/bootstrap.min.css';
// Імпортуйте інші необхідні компоненти та зображення

function App() {
  return (
    <Router>
      <div>
        <Header />
        {/* Використання Switch та Route для налаштування маршрутів */}
      </div>
    </Router>
  );
}

export default App;

