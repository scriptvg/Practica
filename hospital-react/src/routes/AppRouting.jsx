import React from 'react';
import { Route, Routes, BrowserRouter as Router } from 'react-router-dom';

/* Layout publico */
import PublicLayout from '../layouts/PublicLayout';

/* Paginas publicas */
import Login from '../pages/Login';
import Home from '../pages/Home.jsx';

/* Layout admin */
import AdminLayout from '../layouts/AdminLayout';


function AppRouting() {
  return (
    <Router>
      <Routes>

        {/* Rutas públicas */}
        <Route element={<PublicLayout/>}>
            <Route path="/" element={<Home/>} />
            <Route path="/login" element={<Login/>} />
        </Route>

        {/* Rutas protegidas para admin */}
        <Route element={<AdminLayout/>}>
            <Route path="/admin" element={<h1>Admin</h1>} />
        </Route>

        <Route path="*" element={<h1>404</h1>} />
      </Routes>
    </Router>
  )
}

export default AppRouting