var express = require("express");
var router = express.Router();
const nunjucks = require('nunjucks');
const csrf = require('csurf');
var csrfProtection = csrf({ cookie: true });
const { unflatten } = require('flat');

router.get( '/', csrfProtection, routeHome);

router.use('/assets', express.static('./assets'));

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'newsletter_admin',
  password : 'StoreNLetters2021',
  database : 'newsletters'
});

router.get( '/*', function( req, res ) {
  return res.render( '404.html' ) ;
} );

router.post('/api/submit', async function(req, res) {
  if(req.url) {
    const { email } = unflatten(req.body);
    var data = {
      email: email
    };
    connection.connect(function(err) {
      //if(err) {
      //  return res.json({'response': err.message})
      //};
      connection.query('INSERT INTO users SET email = ?', email, function(err, result) {
        var template = 'You will receive updates on the following email address: ' + email + '.';
        rendered = nunjucks.renderString(
          str = template
        );
        return res.json({'response': rendered});
      });
    });
  };
});

function routeHome( req, res ) {
  return res.render( 'home.njk', {
    csrfToken: req.csrfToken(),
  }) ;
}

module.exports = router
