import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

/* Esquema de validación */
const registerSchema = Yup.object().shape({
  username: Yup.string().required('Username is required'),
  email: Yup.string().email('Invalid email').required('Email is required'),
  firstName: Yup.string().required('First Name is required'),
  lastName: Yup.string().required('Last Name is required'),
  password: Yup.string().required('Password is required'),
});

const RegisterForm = ({ handleSubmit, isLoading }) => (
  <Formik
    initialValues={{
      username: '',
      password: '',
      email: '',
      firstName: '',
      lastName: '',
    }}
    validationSchema={registerSchema}
    onSubmit={handleSubmit}
  >
    {({ isSubmitting }) => (
      <Form className="flip-card__form">
        <Field className="flip-card__input" name="username" placeholder="Username" type="text" />
        <ErrorMessage name="username" component="div" className="error-message" />
        <Field className="flip-card__input" name="email" placeholder="Email" type="email" />
        <ErrorMessage name="email" component="div" className="error-message" />
        <Field className="flip-card__input" name="firstName" placeholder="First Name" type="text" />
        <ErrorMessage name="firstName" component="div" className="error-message" />
        <Field className="flip-card__input" name="lastName" placeholder="Last Name" type="text" />
        <ErrorMessage name="lastName" component="div" className="error-message" />
        <Field className="flip-card__input" name="password" placeholder="Password" type="password" />
        <ErrorMessage name="password" component="div" className="error-message" />
        <button className="flip-card__btn" type="submit" disabled={isSubmitting || isLoading}>
          {isLoading ? 'Processing...' : 'Confirm!'}
        </button>
      </Form>
    )}
  </Formik>
);

export default RegisterForm;