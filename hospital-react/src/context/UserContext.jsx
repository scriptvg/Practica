// File: src/context/UserContext.jsx

import React, { createContext, useState, useEffect } from 'react';
import Swal from 'sweetalert2';
import { loginUser, fetchUserProfile } from '../api/api';

const UserContext = createContext();

const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));

  useEffect(() => {
    if (token) {
      fetchProfile();
    }
  }, [token]);

  const login = async (username, password) => {
    try {
      const data = await loginUser(username, password);
      if (data.access) {
        localStorage.setItem('token', data.access);
        setToken(data.access);
        Swal.fire({
          icon: 'success',
          title: 'Login successful!',
          showConfirmButton: false,
          timer: 1500
        });
      } else {
        throw new Error(data.detail || 'An error occurred');
      }
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: error.message,
      });
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
    Swal.fire({
      icon: 'success',
      title: 'Logged out successfully!',
      showConfirmButton: false,
      timer: 1500
    });
  };

  const fetchProfile = async () => {
    if (!token) return;

    try {
      const profile = await fetchUserProfile(token);
      setUser(profile);
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Error fetching profile',
        text: error.message,
      });
    }
  };

  return (
    <UserContext.Provider value={{ user, login, logout, fetchProfile }}>
      {children}
    </UserContext.Provider>
  );
};

export { UserContext, UserProvider };