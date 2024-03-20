import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import './css/index.css';
import Search from './js/Search';
import Home from './js/Home';
import About from './js/About';
import News from './js/News';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Navigate to="/home" />}></Route>
      <Route path="/home" element={<Home />} />
      <Route path="/search" element={<Search />} />
      <Route path="/about" element={<About />} />
      <Route path="/news" element={<News />} />
    </Routes>
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
