/*
var app = angular.module("myApp", ['ngResource']);

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
  return $resource("/project")
});
*/
var app = angular.module('myApp', ['ngAnimate', 'ui.bootstrap', 'ngResource']);

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
  return $resource("/project")
});