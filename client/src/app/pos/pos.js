
/*
angular.module('kenix.scm.controllers', [])
    .controller('urchaseOrderViewCtrl',
        ['$scope', 'purchaseOrderService',
            function ($scope, purchaseOrderService) {
                purchaseOrderService.loadData($scope);
            }]);

angular.module('kenix.scm.po.services', [])
    .service('purchaseOrderService', [function () {
        this.loadData = function ($scope) {
            // Async call to google service
            gapi.client.kenix.pos.list().execut(
                function (resp) {
                    if (!resp.code) {
                        console.debug(resp);
                        $scope.po = resp.items;
                        // because it's a callback,
                        // we need to notify angular of the data refresh
                        $scope.gridOptions = { data: 'po' };
                        $scope.apply();
                    }
                });
        };
    }]);
*/
