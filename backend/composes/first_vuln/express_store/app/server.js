const express = require( 'express' );
const nunjucks = require('nunjucks');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
var program = require('commander');

const routes = require("./controllers/routes");

program.version("0.2")
  .option("-d, --dev", "Development mode: server listens on port 8080")
  .parse(process.argv);

var DEV_MODE = false;
if(program.dev) DEV_MODE = true;

var app = express();

nunjucks.configure(['templates'], {
  autoescape: true,
  express: app
});

app.use(cookieParser());
app.use(bodyParser.urlencoded({limit: '50mb', extended: false }));
app.use(bodyParser.json({limit: '50mb'}));

app.use(routes);

var _port = 8082;
if(DEV_MODE) _port = 8080;

app.listen( _port, '0.0.0.0');
console.log(`DEV_MODE = ${DEV_MODE}, server listening on port ${_port}`);
