var express = require("express");
var router = express.Router();
const nunjucks = require('nunjucks');
const csrf = require('csurf');
var csrfProtection = csrf({ cookie: true });
const { unflatten } = require('flat');

router.get( '/', csrfProtection, routeHome);
router.get('/privacy', routePrivacy);
router.get('/terms', routeTerms);
router.get('/signup', routeSignup);
router.get('/login', routeLogin);
router.use('/assets', express.static('./assets'));
router.get( '/*', function( req, res ) {
  return res.render( '404.html' ) ;
} );

function routeHome( req, res ) {
  return res.render( 'home.njk', {
    csrfToken: req.csrfToken(),
  }) ;
}

function routePrivacy(req,res) {
  return res.render('privacy.njk');
}


function routeTerms(req,res) {
  return res.render('terms.njk');
}

function routeSignup(req,res) {
  return res.render('signup.njk');
}

function routeLogin(req,res) {
  return res.render('login.njk');
}

router.post('/api/signup', async function(req, res){
  if(req.url) {
    return res.json({'response': "We're sorry but registration is currently closed."});
  };
});

router.post('/api/login', async function(req, res){
  if(req.url) {
    return res.json({'response': "We're sorry but user logins are currently disabled."});
  };
});

module.exports = router
