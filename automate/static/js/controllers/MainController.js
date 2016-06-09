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
    $scope.getRunners = function() {
        RequestRunners.query(function(data) {
            $scope.runners = data.data;
        });
    }

    $scope.getRunnerResults = function(event, runner_id) {
        // change click state on runner group list 
        var elm = angular.element(event.currentTarget);
        angular.forEach(elm.parent().children(), function(value, key) {
            angular.element(value).removeClass("active");
        });
        elm.addClass("active");

        // get the runner results for the clicked item
        var result = RequestResults.get({
            id: runner_id
        }, function() {
            console.log(result);
        });
    };

    $scope.clearProject = function() {
        $scope.projectData = {};
        $scope.runners = [];
    }

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

