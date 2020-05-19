// import all variables & spread their values
const NavbarVariables = require("./NavbarVariables.js");
const CampgroundVariables = require("./CampgroundVariables.js");

// USAGE example
// const AboutVariables = {
//     Greeting: 'Welcome to the about page',
//      ... and so on
// };

const pages = {
  Yelpcamp: {
    ...NavbarVariables,
    ...CampgroundVariables,
    signupPath: '/signup',
    loginPath: '/login'
  }
  // ... 'About': { ...AboutVariables }
};

module.exports = pages;