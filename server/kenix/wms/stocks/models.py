from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class StockModel(EndpointsModel):
    """
    Stock model class
    id: SKU + Location
    sku: Customer SKU (product, lot, serial, etc)
        + (receiving date, receiving batch, container, po, so, ...)
    """
    description = ndb.StringProperty()
    condition = ndb.StringProperty()
    uom = ndb.StringProperty()
    decimal_point = ndb.IntegerProperty()
    product = ndb.KeyProperty(kind='ProductModel')
    receipt_dt = ndb.DateTimeProperty()


class SkuModel(EndpointsModel):
    """
    Payout SKU
    """



class OnHandInvModel(EndpointsModel):
    """
    Keep qty of item identified by SKU,
    id: sku:location
    """
    sku = ndb.KeyProperty(kind='OnHandSkuModel')
    location_id = ndb.KeyProperty()
    qty = ndb.IntegerProperty()


class BookInvModel(EndpointsModel):
    """
    Book Inventory

    id: product
    """
    product = ndb.KeyProperty()
    warehouse = ndb.KeyProperty()
