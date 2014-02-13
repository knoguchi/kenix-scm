angular.module('kenix.scm', [
        'services.breadcrumbs',
        'services.i18nNotifications',
        'services.httpRequestTracker',
        'security',
        'templates-app',  // generated js from atpl by html2js
        'templates-common',  // generated js from acpl by html2js
        //'common.errorHandling',
        //'kenix.scm.home',
        //'kenix.scm.about',
        //'kenix.scm.accounts',
        //'kenix.scm.users',
        //'kenix.scm.pos',
        'ui.router'
    ])
    .constant('I18N.MESSAGES', {
        'errors.route.changeError': 'Route change error',
        'crud.user.save.success': "A user with id '{{id}}' was saved successfully.",
        'crud.user.remove.success': "A user with id '{{id}}' was removed successfully.",
        'crud.user.remove.error': "Something went wrong when removing user with id '{{id}}'.",
        'crud.user.save.error': "Something went wrong when saving a user...",
        'crud.project.save.success': "A project with id '{{id}}' was saved successfully.",
        'crud.project.remove.success': "A project with id '{{id}}' was removed successfully.",
        'crud.project.save.error': "Something went wrong when saving a project...",
        'login.reason.notAuthorized': "You do not have the necessary access permissions.  Do you want to login as someone else?",
        'login.reason.notAuthenticated': "You must be logged in to access this part of the application.",
        'login.error.invalidCredentials': "Login failed.  Please check your credentials and try again.",
        'login.error.serverError': "There was a problem with authenticating: {{exception}}."
    })
    .config(function myAppConfig($stateProvider, $urlRouterProvider) {
        console.log('config');
        //$urlRouterProvider.otherwise('/home');
    })
    .run(['security', function (security) {
        console.log('run security');
        // Get the current user when the application starts
        // (in case they are still logged in from a previous session)
        //security.requestCurrentUser();
    }])
    .controller('AppCtrl', ['$scope', '$location', 'security', function ($scope, $location, security) {
        security.requestCurrentUser();
        $scope.$on('$stateChangeSuccess', function (event, toState, toParams, fromState, fromParams) {
            if (angular.isDefined(toState.data.pageTitle)) {
                $scope.pageTitle = toState.data.pageTitle + ' | Kenix NOS';
            }
        });
    }])
    .controller('HeaderCtrl', ['$scope', '$location', 'security', 'breadcrumbs', 'notifications', 'httpRequestTracker',
        function ($scope, $location, security, breadcrumbs, notifications, httpRequestTracker) {
            $scope.location = $location;
            $scope.breadcrumbs = breadcrumbs;

            $scope.isAuthenticated = security.isAuthenticated;
            $scope.isAdmin = security.isAdmin;

            $scope.home = function () {
                if (security.isAuthenticated()) {
                    $location.path('/dashboard');
                } else {
                    $location.path('/projectsinfo');
                }
            };
            $scope.isNavbarActive = function (navBarPath) {
                return navBarPath === breadcrumbs.getFirst().name;
            };

            $scope.hasPendingRequests = function () {
                return httpRequestTracker.hasPendingRequests();
            };
        }]);
