var app = angular.module('myApp', ['ui.bootstrap', 'ngResource']);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');

}]);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');

}]);

app.factory("RequestRunners", function($resource) {
  return $resource("/data/runners", {}, {
    query: { isArray: false }
  })
});

app.factory("RequestResults", function($resource) {
  return $resource("/data/results/:id", {id:1}, {
    query: { isArray: false }
  })
});

app.factory("Project", function($resource) {
  return $resource("/project", {}, {
    query: { isArray: false }
  })
});

// create a shared scope object to share between controllers
app.factory('ProjectData', function () {
    return { name: '', apiuser: '', apikey:'', manifest_file:'', project_ref:'', tests_location:'',status:'', feature_files:'', create_date:'', modified_date:'' };
});