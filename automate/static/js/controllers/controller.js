app.controller("ResourceController", function($scope, RequestRunners, RequestResults, Project) {
  /*********************************************
  Varz 
  **********************************************/
  $scope.runners = [];


  /*********************************************
  Project 
  **********************************************/
  //$scope.project = new Project(); 
  //$scope.project.project_path = "asdasd";

  // create new project
  $scope.createProject = function(projectPath) 
  {
  
    $scope.project.project_path = projectPath;
    Project.save($scope.project, function() {
      //data saved. do something here.
      console.log($scope.project);
    }); //saves an project. Assuming $scope.project is the Project object 
  };

  // load an existing project
  $scope.loadProject = function(projectPath) 
  {

   // var project = Project.get({ project_path: 'C:\\Users\\administrator\\AppData\\Roaming' }, function() {
      var project = Project.get({ project_path: 'C:\\dev\\testing'}, function() {
      if(project.success)
      {
        $scope.getRunners();
      
      }
    });
  };

  /*********************************************
  Runners
  **********************************************/
  $scope.getRunners = function()
  {
    RequestRunners.query(function(data) {
      $scope.runners = data.data;
    });
  }
  


  $scope.getRunnerResults = function(event, runner_id)
  {
    // change click state on runner group list 
    var elm = angular.element( event.currentTarget );
    angular.forEach(elm.parent().children(), function(value, key) {
      angular.element( value ).removeClass("active");
    });
    elm.addClass("active");
    
    // get the runner results for the clicked item
    var result = RequestResults.get({ id: runner_id }, function() {
      console.log(result);
    });
  };

 

  /*********************************************
  Modal Controls
  **********************************************/

  //$scope.createProject('C:\\Users\\administrator\\AppData\\Roaming');
 // $scope.createProject('C:\\Users\\administrator\\AppData\\Roaming');
  


/*  var project = Project.get({ id: $scope.id }, function() {
    console.log(project);
    console.log("ASDASDD");
  }); // get() returns a single project*/
  
/*
  var project = Project.query(function() {
    console.log(project);
  }); //query() returns all the project
*/
  


});
app.directive('myModal', function() {
    return {
        restrict: 'E',
        templateUrl: 'myModalContent.html',
        controller: function ($scope) {
          $scope.selected = {
            item: $scope.items[0] 
          };
        }
    };
});
app.controller('ModalDemoCtrl', function($scope, Modal) {

  
});