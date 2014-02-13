from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel
from kenix.common.models import AddressModel


class BranchModel(EndpointsModel):
    """
    Branch model class
    """
    name = ndb.StringProperty()
    code = ndb.StringProperty()
    mailing_address = ndb.KeyProperty(kind=AddressModel)


class WarehouseModel(EndpointsModel):
    """
    Warehouse class.
    A branch can have multiple warehouses.
    """
    branch = ndb.KeyProperty(kind=BranchModel)
    code = ndb.StringProperty()
    mailing_address = ndb.KeyProperty(kind=AddressModel)


class LocationModel(EndpointsModel):
    """
    Location class
    """
    warehouse = ndb.KeyProperty(kind=WarehouseModel)
    code = ndb.StringProperty()


class RcvOrderModel(EndpointsModel):
    """
    Receiving Order Model
    """
    eta = ndb.DateTimeProperty(verbose_name="Estimated Arrival")


class ReceiptModel(EndpointsModel):
    """
    Receipt class
    """
    receipt_date = ndb.DateTimeProperty()
