import React from "react";
import ReactDOM from "react-dom";
import App from "./App.js"
import Clock from "./Clock.js";
import Toggle from "./Toggle.js";
import LoginControl from "./LoginControl.js";
import NumberList from "./NumberList.js";
import Reservation from "./Reservation.js";
import NameForm from "./NameForm.js";
import FileInput from "./FileInput.js";
import Calculator from "./Calculator.js";
import ModalTest from "./Modal.js";
import CustomTextInput from "./CustomTextInput.js";
import MouseTracker from "./MouseTracker.js";

ReactDOM.render(
  <>
    <MouseTracker />
    <CustomTextInput />
    <ModalTest />
    <Calculator />
    <FileInput />
    <NameForm />
    <Reservation />
    <NumberList />
    <LoginControl />
    <Toggle />
    <Clock />
    <App />
  </>, 
  document.getElementById("root"));


