import React, { useState, useContext, useEffect } from 'react';
import { UserContext } from '../context/UserContext';
import { registerUser } from '../api/api';
import Swal from 'sweetalert2';
import LoginForm from './LoginForm';
import RegisterForm from './RegisterForm';
import './Login.css';

const LoginComponent = () => {
  const { login, fetchProfile } = useContext(UserContext);
  const [isLogin, setIsLogin] = useState(true);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (values, { setSubmitting }) => {
    setIsLoading(true);
    try {
      if (isLogin) {
        await login(values.username, values.password);
        Swal.fire({
          icon: 'success',
          title: 'Welcome back!',
          text: 'You have successfully logged in.',
          showConfirmButton: false,
          timer: 1500
        });
      } else {
        const userData = {
          username: values.username,
          email: values.email,
          first_name: values.firstName,
          last_name: values.lastName,
          password: values.password
        };
        const responseData = await registerUser(userData);
        if (responseData.access) {
          localStorage.setItem("token", responseData.access);
          Swal.fire({
            icon: 'success',
            title: 'Registration successful!',
            showConfirmButton: false,
            timer: 1500
          });
        } else {
          throw new Error(responseData.detail || 'An error occurred');
        }
      }
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: error.message || 'An unexpected error occurred',
      });
    } finally {
      setIsLoading(false);
      setSubmitting(false);
    }
  };

  return (
    <div className="wrapper">
      <div className="card-switch">
        <label className="switch">
          <input type="checkbox" className="toggle" onChange={() => setIsLogin(!isLogin)} disabled={isLoading} />
          <span className="slider"></span>
          <span className="card-side"></span>
          <div className="flip-card__inner">
            <div className="flip-card__front">
              <div className="title">{isLogin ? 'Log in' : 'Sign up as Patient'}</div>
              {isLogin ? (
                <LoginForm handleSubmit={handleSubmit} isLoading={isLoading} />
              ) : (
                <RegisterForm handleSubmit={handleSubmit} isLoading={isLoading} />
              )}
              {isLogin && (
                <p className="forgot-password">
                  <a href="#" onClick={(e) => { e.preventDefault(); /* Add forgot password logic */ }}>
                    Forgot Password?
                  </a>
                </p>
              )}
            </div>
            <div className="flip-card__back">
              <div className="title">Sign up as Patient</div>
              <RegisterForm handleSubmit={handleSubmit} isLoading={isLoading} />
            </div>
          </div>
        </label>
      </div>
    </div>
  );
};

export default LoginComponent;