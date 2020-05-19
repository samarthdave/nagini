const express = require("express");
const {
  renderPage
} = require("./lib/resolvers");
const app = express();

app.set("view engine", "ejs");
app.use("/static", express.static("static"));

// PAGES
app.get("/",            renderPage("Yelpcamp", "landing"));
app.get("/login",       renderPage("Yelpcamp", "login"));
app.get("/signup",      renderPage("Yelpcamp", "signup"));
app.get("/about",       renderPage("Yelpcamp", "about"));
app.get("/campgrounds", renderPage("Yelpcamp", "index"));

exports.app = app;