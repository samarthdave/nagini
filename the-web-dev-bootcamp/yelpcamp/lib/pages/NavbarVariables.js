// create all variables for each component
const NavbarVariables = {
  navbarBrand: 'Yelpcamp',
  navbarBrandHref: '/',
  navbarLeft: [{
    name: "Campgrounds",
    href: "/campgrounds",
  }, {
    name: "About",
    href: "/about",
  }, {
    name: "New",
    href: "/campgrounds/new",
  }],
  navbarRight: [{
    name: "Login",
    href: "/login",
  }, {
    name: "Sign up",
    href: "/signup",
  }]
};

module.exports = NavbarVariables;