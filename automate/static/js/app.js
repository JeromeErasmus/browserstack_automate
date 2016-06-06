
var app = angular.module("myApp", ['ngResource', 'ui.bootstrap']);

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

app.factory("Modal", function($scope, $modal, $log) {
  
  $scope.items = ['item1', 'item2', 'item3'];

  $scope.open = function (size) {
    var modalInstance;
    var modalScope = $scope.$new();
    modalScope.ok = function () {
            modalInstance.close(modalScope.selected);
    };
    modalScope.cancel = function () {
            modalInstance.dismiss('cancel');
    };      
    
    modalInstance = $modal.open({
      template: '<my-modal></my-modal>',
      size: size,
      scope: modalScope
      }
    );

    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });
  };
});
