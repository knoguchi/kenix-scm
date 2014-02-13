// https://groups.google.com/forum/#!searchin/angular/gapi/angular/uVaPf3VVgRQ/SwqGyBTzT7kJ
// https://groups.google.com/forum/#!searchin/angular/gapi/angular/zU4AhW-PSEM/b1ieO7Zw8iwJ
// http://stackoverflow.com/questions/18537687/what-is-the-difference-between-init-and-window-init
// http://stackoverflow.com/questions/15666048/angular-js-service-vs-provider-vs-factory
angular.module('kenix', [])
    .factory('kenix', ['$rootScope', '$q', function ($rootScope, $q) {
        var service = {
            asyncLogin: function (email, password) {
                var deferred = $q.defer();
                setTimeout(function () {
                    deferred.notify('About to authenticate ' + email + '.');
                    gapi.client.kenix_core.users.auth({email: email, password: password})
                        .execute(
                        function (response) {
                            deferred.resolve(response);
                        },
                        function (response) {
                            deferred.reject(response);
                        }
                    );
                }, 1000);
                return deferred.promise;
            },
            asyncLogout: function () {
                var deferred = $q.defer();
                setTimeout(function () {
                    deferred.notify('About to logout');
                    gapi.client.kenix_core.users.logout().execute(function (response) {
                        deferred.resolve(response);
                    }, function (response) {
                        deferred.reject(response);
                    });
                }, 1000);
                return deferred.promise;
            },
            login: function (email, password) {
                return gapi.client.kenix_core.users.auth(email, password)
                    .execute(function (response) {
                        return response.data.user;
                    });
            },
            logout: function () {
                return gapi.client.kenix_core.users.logout()
                    .execute(function (response) {
                        return response.result.logout_status;
                    });
            },
            auth: function () {
                return gapi.client.kenix_core.users.auth()
                    .execute(function (response) {
                        if (response && response.code == 200) {
                            return response.result.user;
                        }
                        return null;
                    });
            }
        };
        return service;

    }
    ]);


//this.login = function () {
//    gapi.auth.authorize({ client_id: clientId, scope: scopes, immediate: false, hd: domain }, this.handleAuthResult);
//
//    return deferred.promise;
//};
//
//this.handleClientLoad = function () {
//    gapi.client.setApiKey(apiKey);
//    gapi.auth.init(function () {
//    });
//    window.setTimeout(checkAuth, 1);
//};
//
//this.checkAuth = function () {
//    gapi.auth.authorize({ client_id: clientId, scope: scopes, immediate: true, hd: domain }, this.handleAuthResult);
//};
//
//this.handleAuthResult = function (authResult) {
//    if (authResult && !authResult.error) {
//        var data = {};
//        gapi.client.load('users', 'v1', function () {
//            $scope.isBackendReady = true;
//            $scope.list();
//        }, 'http://localhost:8080/_ah/api');
//
//        gapi.client.load('oauth2', 'v2', function () {
//            var request = gapi.client.oauth2.userinfo.get();
//            request.execute(function (resp) {
//                $rootScope.$apply(function () {
//                    data.email = resp.email;
//                });
//            });
//        });
//        deferred.resolve(data);
//    } else {
//        deferred.reject('error');
//    }
//};
//
//this.handleAuthClick = function (event) {
//    gapi.auth.authorize({ client_id: clientId, scope: scopes, immediate: false, hd: domain }, this.handleAuthResult);
//    return false;
//};
//
//
//}])
//;
