app.controller('MainController', function($scope, $http) { 

  $scope.parameters = {};

  $scope.update = function(parameters)
  {
  	$scope.parameters = angular.copy(parameters);
  }

  $scope.loadData = function()
  {

  	$http.get("/loaddata/").success(function (data) {
  		$scope.parameters = data.parameters;
  	
  	}).error(function () {
  		console.log("error loading data");
  	});
  }
});


