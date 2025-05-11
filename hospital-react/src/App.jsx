import React from "react";
import './App.css'
import Login from "./components/LoginComponent";
import { UserProvider } from "./context/UserContext";
import AppRouting from "./routes/AppRouting";

function App() {
  return (
    <>
    <UserProvider>
      <AppRouting />
    </UserProvider>
    </>
  )
}

export default App
