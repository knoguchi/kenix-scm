import logging

import endpoints
from protorpc import messages
from protorpc import remote
from google.appengine.api import users

from models import UserModel
from kenix.core.api import kenix_core_api

log = logging.getLogger(__name__)


class AuthRequest(messages.Message):
    email = messages.StringField(1)
    password = messages.StringField(2)


class AuthToken(messages.Message):
    """
    Authentication Token
    """
    auth_token = messages.StringField(1)
    user = messages.StringField(2)
    logout_status = messages.BooleanField(3)


@kenix_core_api.api_class(resource_name='users')
class UserService(remote.Service):
    """
    Users API v1
    """

    @UserModel.query_method(query_fields=('limit', 'pageToken', 'email'),
                            path='users', name='index')
    def index(self, query):
        """
        List of users
        """
        return query

    @UserModel.method(path='users/{id}', http_method='GET', name='get')
    def get(self, user):
        """
        Get a user
        @param user:
        @return:
        """
        if not user.from_datastore:
            raise endpoints.NotFoundException('User not found')
        return user

    @UserModel.method(path='users', name='create')
    def create(self, user):
        """
        Create a user
        """
        # do some validation
        user.put()
        return user

    @UserModel.method(path='users/{id}', http_method='PUT', name='update')
    def update(self, user):
        """
        Update a user
        @param user:
        @return user:
        """

        if not user.from_datastore:
            raise endpoints.NotFoundException('User not found')
        user.put()
        return user

    # @UserModel.method(path='users', http_method='POST',
    #                   name='_auth')
    # def _auth(self, query):
    #     """
    #     Authenticate user by user id and password, or cookie.
    #     """
    #     log.error(query)
    #     current_user = endpoints.get_current_user()
    #     if not current_user:
    #         raise endpoints.NotFoundException('User not authenticated')
    #     return current_user

    # request_message=message_types.VoidMessage,
    # response_message=message_types.VoidMessage,
    # name=None,
    # path=None,
    # http_method='POST',
    # cache_control=None,
    # scopes=None,
    # audiences=None,
    # allowed_client_ids=None,
    # auth_level=None

    @endpoints.method(AuthRequest, AuthToken,
                      path='users/auth', http_method='POST',
                      name='auth')
    def auth(self, *args, **kw):
        """
        Authenticate a user by email and password
        @param args:
        @param kw:
        @return:
        """
        user = users.get_current_user()
        token = AuthToken()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        #else:
        #    self.redirect(users.create_login_url(self.request.uri))

        log.error(args)
        log.error(kw)
        token.auth_token = 'aaa'
        token.user = 'kenji'
        return token

    @endpoints.method(AuthRequest, AuthToken,
                      path='users/logout', http_method='POST',
                      name='logout')
    def logout(self, *args, **kw):
        """
        Logout a user
        @param self:
        @param args:
        @param kw:
        @return:
        """
        token = AuthToken()
        token.auth_token = ''
        token.user = ''
        token.logout_status = True
        return token

