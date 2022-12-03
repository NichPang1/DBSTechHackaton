//import logo from './logo.svg';
import React, {useState} from "react";
import { Login } from "./Login";
import { Register } from "./Register";
import "./App.css"
import img from './DBS.png'


function App() {
  const [currentForm, setCurrentForm] = useState("login"); //for login page to be displayed first
  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }
  return (
    
    <div className = "App">
      <img src={img}/>
      {
        currentForm === "login" ? <Login onFormSwitch={toggleForm}/>: < Register onFormSwitch={toggleForm}/>
      }
             </div>
  );
}

export default App;
