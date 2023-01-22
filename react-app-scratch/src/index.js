import React from "react";
import ReactDOM from "react-dom";
import App from "./App.js"
import Clock from "./Clock.js";
import Toggle from "./Toggle.js";

ReactDOM.render(
  <>
    <Toggle />
    <Clock />
    <App />
  </>, 
  document.getElementById("root"));
