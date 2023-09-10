# DjangoReactJsProjectSetup
This repository provides the folder structure and configuration files to setup an integrated Django and ReactJs project.
The Backend virtual env directory contains both the Django application in the directory called Backdend and the ReactJs project in the directory called Frontend.

# Project setup procedure
Initially the ReactJs project must be built, we use webpack to resolve all dependencies and bundle the required ReactJs and Vanilla Javascript files in a single bundle.js.
In order to do so, webpack and its dependency node modules must be installed. The required development and production stage dependencies for the project are shown in the package.json file.

For setting the project from barebones, the instructions will allow you to complete the setup of both the Django and React projects.
1) Install package.json file using node package manager, with 'npm install -y'
2) Install React with npm:
npm install react react-dom 
react and react-dom node packages will be apart of your production dependencies, you can view them in package.json
3) Install Babel with npm:
npm install babel --save-dev @babel/core @babel/preset-env @babel/preset-react babel-loader
--save-dev installs the following babel packages as dependencies only for development, you can view them in package.json
4) Create the .babelrc file with the following definition, to configure the babel node package to use the following presets:
{ 
    "presets": ["@babel/preset-react", "@babel/preset-env"] 
}
5) Install Webpack, loaders and plugins with npm for dependency resolving and project building:
npm install --save-dev webpack webpack-cli webpack-dev-server style-loader file-loader css-loader html-webpack-plugin
--save-dev installs the following webpack, loaders and plugins as development dependencies
6) Create the webpack.config file to configure webpack to begin building from entry points and outputting a final bundle file, add a definition suitable for your project, example below:
const HtmlWebpackPlugin = require("html-webpack-plugin"); 
const path = require("path"); 

module.exports = { 
  entry: "./src/main.js", 
  output: { 
    filename: "bundle.[hash].js", 
    path: path.resolve(__dirname, "dist"), 
  }, 
  mode: 'development', 
  plugins: [ 
    new HtmlWebpackPlugin({ 
      template: "./src/index.html", 
    }), 
  ], 
  resolve: { 
    modules: [__dirname, "src", "node_modules"], 
    extensions: ["*", ".js", ".jsx", ".tsx", ".ts"], 
  }, 
  module: { 
    rules: [ 
      { 
        test: /\.jsx?$/, 
        exclude: /node_modules/, 
        loader: require.resolve("babel-loader"), 
      }, 
      { 
        test: /\.css$/, 
        use: ["style-loader", "css-loader"], 
      }, 
      { 
        test: /\.png|svg|jpg|gif$/, 
        use: ["file-loader"], 
      }, 
    ], 
  }, 
};
7) Create the entry directory and files from which webpack begins project building and dependency resolving, in the above example:
Webpack is configured to begin building from the src entry directory with the main.js file, and template generation using the index.html
(Note: the index.html file should include a div with an id of root and the main.js file should import and render your app component from app.js)
8) Configure the package.json scripts key by adding a javascript object with string key's and string npm commands for running the ReactJs project locally using webpack development server and building the production files for the ReactJs project(index.html and bundle.js)
to build the final bundle and HTML files
The React project has been build correctly

1) Create a virtual environment for Python, initalize a project and create a django application.
In our project, the top level Backend directory is our virtual environment, the second level directory is our Django project and the Core_CRUD directory is our django application
2) Move the frontend application directory into the django project directory
3) In settings.py, define the templates variable with a list containing a string path to the directory containing the html files of the frontend application 
In our example, this becomes [BASE_DIR / 'FrontEnd/dist/templates']
4) In settings.py, define STATIC_URL with a string URL path of your choosing, this URL path will be removed from the URL request for a static file.
e.g STATIC_URL = '/assets/'
5) In settings.py, define STATICFILES_DIRS containing a list of directory paths for searching any static files, define a string containing the directory path to where the static files appear in the frontend directory. In our example, [BASE_DIR / 'FrontEnd/dist'] will be searched, followed by the remaining URl to the request static file as a result of truncation.
e.g <script defer="defer" src="/assets/Core_CRUD/bundle.js">, /assets/ will be removed, determined by the STATIC_URL = '/assets/' variable in settings.py. Core_CRUD/bundle.js is searched in [BASE_DIR / 'FrontEnd/dist'].
The paths will be searched when URL requests to the static file is made. e.g Embedding URL to static file in html template or ajax requests 

Alternatively for a simpler approach, its possible to clone the project to your working directory using "git clone". Changing the configuration of webpack.config.js, package.json, django settings.py and dist folder build files to suit your application requirements.
