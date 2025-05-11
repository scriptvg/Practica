import React from 'react';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';
import Login from '../pages/Login';
import Home from '../pages/Home.jsx';


function AppRouting() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/login" element={<Login/>} />
      </Routes>
    </Router>
  )
}

export default AppRouting