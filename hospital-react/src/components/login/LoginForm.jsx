import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const loginSchema = Yup.object().shape({
  username: Yup.string().required('Username is required'),
  password: Yup.string().required('Password is required'),
});

const LoginForm = ({ handleSubmit, isLoading }) => (
  <Formik
    initialValues={{
      username: '',
      password: '',
    }}
    validationSchema={loginSchema}
    onSubmit={handleSubmit}
  >
    {({ isSubmitting }) => (
      <Form className="flip-card__form">
        <Field className="flip-card__input" name="username" placeholder="Username" type="text" />
        <ErrorMessage name="username" component="div" className="error-message" />
        <Field className="flip-card__input" name="password" placeholder="Password" type="password" />
        <ErrorMessage name="password" component="div" className="error-message" />
        <button className="flip-card__btn" type="submit" disabled={isSubmitting || isLoading}>
          {isLoading ? 'Processing...' : 'Let\'s go!'}
        </button>
      </Form>
    )}
  </Formik>
);

export default LoginForm;