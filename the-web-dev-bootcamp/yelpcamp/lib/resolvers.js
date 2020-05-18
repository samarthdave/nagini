// get all variables for each page
const pages = require("./pages");

/**
 * Render an EJS template
 * @param pageName      The title of this page
 * @param templateFile  Name of the ejs template to use
 */
exports.renderPage = (pageName, templateFile) => {
  return (req, res) => {
    const newReq = {
      ...req,
      // this access the variables for that page
      ...pages[pageName],
      pageName,
      templateFile
    };
    res.render(templateFile, {
      yelpcamp: newReq
    });
  };
};