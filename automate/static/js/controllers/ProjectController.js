
// --------------------------------------------
// Project Controls
// --------------------------------------------

app.controller('ProjectCtrl', function($scope, $uibModal, $log, ProjectData, Project) {
    $scope.projectData = ProjectData;
    // load an existing project
    $scope.loadProject = function(size) {
        var modalInstance = $uibModal.open({
            templateUrl: 'ModalProjectLoad.html',
            controller: 'ModalProjectLoadInstanceCtrl',
            size: size,
            resolve: {
                Project: function() {
                    return Project;
                }
            }
        });


        modalInstance.result.then(function(selectedItemData) {
            if (!selectedItemData)
                return;

            var project = Project.get({
                project_path: selectedItemData.manifest_file
            }, function() {

                if (project && project.status == "success") {
                    $scope.clearProject();
                    $scope.projectData = project.data.project;
                }
            });

        }, function() {
            $log.info('Modal dismissed at: ' + new Date());
        });

        /*  var project = Project.get({ project_path: 'C:\\dev\\testing'}, function() {
          if(project.success)
          {
            $scope.getRunners();
          }
        });*/
    };

    $scope.createProject = function(size) {

        var modalInstance = $uibModal.open({
            templateUrl: 'ModalProjectCreate.html',
            controller: 'ModalProjectCreateInstanceCtrl',
            size: size
        });

        modalInstance.result.then(function(formData) {

            // create new project
            var project = Project.save(formData, function() {
                if (project && project.status == "success") {
                    $scope.clearProject();
                    $scope.projectData = project.data;
                   /* $.each(project.data, function(key, value) {
                        $scope.projectData[key] = value;
                    });*/
                }
            });
        }, function() {
            $log.info('Modal dismissed at: ' + new Date());
        });
    };
});


app.controller('ModalProjectCreateInstanceCtrl', function($scope, $uibModalInstance) {
    $scope.formData = {
        name: '',
        apiuser: '',
        apikey: '',
        manifest_file: '',
        project_ref: '',
        tests_location: '',
        status: ''
    };

    $scope.ok = function() {
        $uibModalInstance.close($scope.formData);
    };

    $scope.cancel = function() {
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


    
app.controller('ModalProjectLoadInstanceCtrl', function($scope, $uibModalInstance, Project) {
    $scope.selectedItem = {};
    $uibModalInstance.rendered.then(function() {

        // get a list of all project
        Project.query(function(projects) {

            var $table = $(".modal #load_project_table");
            $table.bootstrapTable({
                data: projects.data
            });

            $table.on('click-row.bs.table', function(e, row, $element) {
                $('.success').removeClass('success');
                $($element).addClass('success');
            });
        });
    });

    $scope.ok = function() {
        var $table = $(".modal #load_project_table");
        var index = $table.find('tr.success').data('index');
        var selectedItemData = $table.bootstrapTable('getData')[index];

        $uibModalInstance.close(selectedItemData);
    };

    $scope.cancel = function() {
        $uibModalInstance.dismiss('cancel');
    };
});