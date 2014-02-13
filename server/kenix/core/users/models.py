from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class UserModel(EndpointsModel):
    """
    User model class.
    A user must belong to one or more accounts
    """
    nickname = ndb.StringProperty()
    full_name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    accounts = ndb.KeyProperty(kind='AccountModel', repeated=True)


class RoleModel(EndpointsModel):
    """
    Role model class.  Role is defined by accounts
    A user must belong to one or more roles
    """
    account = ndb.KeyProperty(kind='AccountModel')
    name = ndb.StringProperty()
    code = ndb.StringProperty()


class PermissionModel(EndpointsModel):
    """
    Permission model class.
    Permission is given to role.
    """
    account = ndb.KeyProperty(kind='AccountModel')
    name = ndb.StringProperty()
    code = ndb.StringProperty()
