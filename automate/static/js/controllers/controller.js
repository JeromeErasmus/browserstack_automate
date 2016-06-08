
app.controller("ResourceController", function($scope, RequestRunners, RequestResults, Project, ProjectData) {

  $scope.projectData = ProjectData;
  $scope.runners = [];

  // --------------------------------------------
  // Project 
  // --------------------------------------------
  //$scope.project = new Project(); 
  //$scope.project.project_path = "asdasd";

  

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


// --------------------------------------------
// Project Controls
// --------------------------------------------

app.controller('ProjectCtrl', function($scope, $uibModal, $log, ProjectData, Project) 
{
  $scope.projectData = ProjectData;


  // load an existing project
  $scope.loadProject = function(size) 
  {
    
    var modalInstance = $uibModal.open({
      templateUrl: 'ModalProjectLoad.html',
      controller: 'ModalProjectLoadInstanceCtrl',
      size: size
      
    });

    modalInstance.rendered.then(function() {

      // get a list of all project
      Project.query(function(projects) {
     
        $(".modal #load_project_table").bootstrapTable({
          data: projects.data
        });
      });

      
    });

    modalInstance.result.then(function(formData) {

    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });

    /*  var project = Project.get({ project_path: 'C:\\dev\\testing'}, function() {
      if(project.success)
      {
        $scope.getRunners();
      }
    });*/
  };

  // --------------------------------------------
  // Modal controls
  // --------------------------------------------
  $scope.createProject = function (size) {
    
    var modalInstance = $uibModal.open({
      templateUrl: 'ModalProjectCreate.html',
      controller: 'ModalProjectCreateInstanceCtrl',
      size: size
    });

    modalInstance.result.then(function(formData) {

      // create new project
      var result = Project.save(formData, function() 
      {
        if(result && result.status == "success")
        {
          $.each( result.data, function( key, value ) {
            $scope.projectData[key] = value;
          });
        }
      }); 


    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });
  };
});


app.controller('ModalProjectCreateInstanceCtrl', function ($scope, $uibModalInstance) 
{
  $scope.formData = { name: '', apiuser: '', apikey:'', manifest_file:'', project_ref:'', tests_location:'',status:'' };

  $scope.ok = function () {
    $uibModalInstance.close($scope.formData);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };

  // handle pretty looking folder browser
  $(document).on('change', '.modal :file', function() {
      console.log("Opening file chooser");
      var input = $(this),
          numFiles = input.get(0).files ? input.get(0).files.length : 1,
          label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
      input.trigger('fileselect', [numFiles, label]);
      console.log(input);
      //$(".modal #projectFolderBrowse").val(label);
      $scope.projectData.location = label;
  });
/*

  $('.modal :file').on('fileselect', function(event, numFiles, label) {
    console.log("on file select");
      $(".modal #projectFolderBrowse").val(label);
      console.log(numFiles);
      console.log(label);
  });*/

});



app.controller('ModalProjectLoadInstanceCtrl', function ($scope, $uibModalInstance) 
{
 
  

  $scope.ok = function () {
    $uibModalInstance.close();
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };

 /* $scope.formData = { name: '', apiuser: '', apikey:'', manifest_file:'', project_ref:'', tests_location:'',status:'' };

  $scope.ok = function () {
    $uibModalInstance.close($scope.formData);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };

  // handle pretty looking folder browser
  $(document).on('change', '.modal :file', function() {
      console.log("Opening file chooser");
      var input = $(this),
          numFiles = input.get(0).files ? input.get(0).files.length : 1,
          label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
      input.trigger('fileselect', [numFiles, label]);
      console.log(input);
      //$(".modal #projectFolderBrowse").val(label);
      $scope.projectData.location = label;
  });*/

});