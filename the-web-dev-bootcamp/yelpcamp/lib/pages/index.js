// import all variables & spread their values
const NavbarVariables = require("./NavbarVariables.js");

// USAGE example
// const AboutVariables = {
//     Greeting: 'Welcome to the about page',
//      ... and so on
// };

// pack all together with 'Home', 'About', etc.
// representing the title of each page
const pages = {
  Home: {
    ...NavbarVariables
  }
  // ... 'About': { ...AboutVariables }
};

module.exports = pages;