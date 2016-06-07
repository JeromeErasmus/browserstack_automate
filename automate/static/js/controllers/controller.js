
app.controller("ResourceController", function($scope, RequestRunners, RequestResults, Project, ProjectData) {
  // --------------------------------------------
  // Varz 
  // --------------------------------------------
  $scope.projectData = ProjectData;
  $scope.runners = [];

  // --------------------------------------------
  // Project 
  // --------------------------------------------
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

  // --------------------------------------------
  // Runners
  // --------------------------------------------
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

 

  // --------------------------------------------
  // Modal Controls
  // --------------------------------------------

  //$scope.createProject('C:\\Users\\administrator\\AppData\\Roaming');
 // $scope.createProject('C:\\Users\\administrator\\AppData\\Roaming');
  


// var project = Project.get({ id: $scope.id }, function() {
//    console.log(project);
//    console.log("ASDASDD");
//  }); // get() returns a single projec
  
//  var project = Project.query(function() {
//    console.log(project);
//  }); //query() returns all the project


});

app.controller('ModalDemoCtrl', function($scope, $uibModal, $log, ProjectData) {

  $scope.projectData = ProjectData;

  $scope.items = ['item1', 'item2', 'item3'];
  /*$scope.projectData.name = "Test";
  $scope.projectData.apiuser = "Test";
  $scope.projectData.apikey = "Test";*/

  $scope.open = function (size) {
    console.log("open");
    var modalInstance = $uibModal.open({
      templateUrl: 'myModalContent.html',
      controller: 'ModalInstanceCtrl',
      size: size,
      resolve: {
        items: function () { return $scope.items; },
        projectData: function () { return $scope.projectData; }
      }
    });

    modalInstance.result.then(function(data) {
      $scope.selected = data.selectedItem;
      $scope.projectData = data.projectData;
      console.log(data);
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });

  };


});

// Please note that $uibModalInstance represents a modal window (instance) dependency.
// It is not the same as the $uibModal service used above.

app.controller('ModalInstanceCtrl', function ($scope, $uibModalInstance, items, projectData) {
  $scope.projectData = projectData;

  $scope.items = items;
  $scope.selected = {
    item: $scope.items[0]
  };

  $scope.data = {};

  $scope.ok = function () {
    $scope.data = {projectData:$scope.projectData, selectedItem: $scope.selected.item};
    $uibModalInstance.close($scope.data);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
});