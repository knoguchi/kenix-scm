from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel
from kenix.common.models import ContactModel, AddressModel


class AccountModel(EndpointsModel):
    """
    Account model class
    """
    code = ndb.StringProperty()
    # company address
    mailing_address = ndb.KeyProperty(kind=AddressModel)

    # billing contact and address
    billing_contact = ndb.KeyProperty(kind=ContactModel)
    billing_address = ndb.KeyProperty(kind=AddressModel)