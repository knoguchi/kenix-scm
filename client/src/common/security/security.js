// Based loosely around work by Witold Szczerba - https://github.com/witoldsz/angular-http-auth
angular.module('security.service', [
        'kenix',
        'security.retryQueue',    // Keeps track of failed requests that need to be retried once the user logs in
        'security.login',         // Contains the login form template and controller
        'ui.bootstrap'     // Used to display the login form as a modal dialog.
    ])

    .factory('security', ['kenix', '$q', '$location', 'securityRetryQueue', '$modal', function (kenix, $q, $location, queue, $modal) {

        // Redirect to the given url (defaults to '/')
        function redirect(url) {
            url = url || '/';
            $location.path(url);
        }

        // Login form dialog stuff
        var loginDialog = null;

        function openLoginDialog() {
            if (loginDialog) {
                throw new Error('Trying to open a dialog that is already open!');
            }
            loginDialog = $modal.open({
                templateUrl: 'security/login/form.tpl.html',
                controller: 'LoginFormController'
            });
            loginDialog.result.then(onLoginDialogClose);
        }

        function closeLoginDialog(success) {
            if (loginDialog) {
                loginDialog.close(success);
            }
        }

        function onLoginDialogClose(success) {
            loginDialog = null;
            if (success) {
                queue.retryAll();
            } else {
                queue.cancelAll();
                redirect();
            }
        }

        // Register a handler for when an item is added to the retry queue
        queue.onItemAddedCallbacks.push(function (retryItem) {
            if (queue.hasMore()) {
                service.showLogin();
            }
        });

        // The public API of the service
        var service = {

            // Get the first reason for needing a login
            getLoginReason: function () {
                return queue.retryReason();
            },

            // Show the modal login dialog
            showLogin: function () {
                openLoginDialog();
            },

            // Attempt to authenticate a user by the given email and password
            login: function (email, password) {
                // this function should return a Promise.
                // Do not block!!
                // a promise takes a callback function with .then(func)
                console.log("login with %s, %s", email, password);
                var login_promise = kenix.asyncLogin(email, password);
                return login_promise.then(function (response) {
                    service.currentUser = response.user;
                    if (service.isAuthenticated()) {
                        closeLoginDialog(true);
                    }
                    return service.isAuthenticated();
                });
            },
            // Give up trying to login and clear the retry queue
            cancelLogin: function () {
                closeLoginDialog(false);
                redirect();
            },

            // Logout the current user and redirect
            logout: function (redirectTo) {
                redirectTo = '/';
                console.log("logout and redirect to %s", redirectTo);
                var logout_promise = kenix.asyncLogout();
                return logout_promise.then(function (response) {
                    if (response.logout_status) {
                        service.currentUser = null;
                        console.log("redirecting %s", redirectTo);
                        redirect(redirectTo);
                    }
                });

            },

            // Ask the backend to see if a user is already authenticated - this may be from a previous session.
            requestCurrentUser: function () {
                if (service.isAuthenticated()) {
                    return $q.when(service.currentUser);
                } else {
                    var currentUser = kenix.auth();
                    if (currentUser) {
                        service.currentUser = currentUser;
                        return service.currentUser;
                    }
                }
            },

            // Information about the current user
            currentUser: null,

            // Is the current user authenticated?
            isAuthenticated: function () {
                console.log("isAuthenticated %s", service.currentUser);
                return !!service.currentUser;
            },

            // Is the current user an administrator?
            isAdmin: function () {
                return !!(service.currentUser && service.currentUser.admin);
            }
        };

        return service;
    }]);
