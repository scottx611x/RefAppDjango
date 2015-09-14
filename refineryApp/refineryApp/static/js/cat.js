var app = angular.module('refineryApp', ['restangular']);

// configure restangular to work with tastypie, which returns data in an objects list, meta data in a meta object
app.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl("/api/v1/");
    RestangularProvider.setResponseExtractor(function(response, operation, what, url) {
        var newResponse;
        if (operation === "getList") {
            newResponse = response.objects;
            newResponse.metadata = response.meta;
        } else {
            newResponse = response;
        }
        return newResponse;
    });
    RestangularProvider.setRequestSuffix('/?');
});


function CategoryController($scope, Restangular){
    $scope.categorys = [];

    $scope.getAllCategorys = function(){
        Restangular.all("category").getList().then(function(categorys){
            $scope.categorys = categorys;
        });
    }

    $scope.getAllCategorys();
}/**
 * Created by scott on 9/11/15.
 */
