# DjangoReactJsProjectSetup
This repository provides the folder structure and configuration files to setup an integrated Django and ReactJs project.
The Backend folder contains a Frontend folder, in this case the Frontend contains a ReactJs project.

# Project setup procedure
Initially the ReactJs project must be built, we use webpack to bundle the required ReactJs and Vanilla Javascript files in a single bundle.js.
In order to do so, webpack and its dependency node modules must be installed. The required dependencies are shown in the package.json file.

If you intend to setup from barebones, the instructions provided below can help you to achieve the setup of a ReactJs project
1) The package.json packages must first be installed with 'npm install' followed by the definition of the .babelrc file.
2) src folder must be created with Index.html, App.js and Index.js files, where the Index.html contains a div html element with an id of "root",
App.js containing your main ReactJs application component and Index.js performs the rendering of your App.js component into your root div element.
3) webpack.config.js must be configured to build a bundle.js file using the source folder; HTML, CSS and File loaders may need to be installed 
and configured in the file, however they will be included in the package.json file.
A folder named "dist" by default will be generated and containing the index.html file with the final bundle.js file embedded, the bundle.js file and licensing documentation.
4) package.json should be configured with command line scripts to run the ReactJs project on the local webpack development server and using webpack
to build the final bundle and HTML files.
5) Initialize a Django project.
6) Define the settings.py templates variable to search within the Frontend webpack generated "dist" folder 
7) Define STATICFILES_DIRS containing a list of directory search paths for static files, the paths will be searched when static URL requests are made. 
The paths should include the path to the Frontend/dist folder.
8) Define STATIC_URL to a URL path of your choosing, this URL path will be removed from the URL request to a static file and matched with paths
in the STATICFILES_DIR
e.g <script defer="defer" src="/assets/Core_CRUD/bundle.js">, /assets/ will be truncated and the remaining path matched in paths within STATICFILES_DIRS

Alternatively for a simpler approach, its possible to clone the project to your working directory using "git clone". Changing the configuration of webpack.config.js, package.json, django settings.py and dist folder build files to suit your application requirements.
