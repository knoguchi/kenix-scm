from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class ProductModel(EndpointsModel):
    """
    Product class.
    id: kenix sku
    sku: account sku
    description:
    """
    sku_id = ndb.StringProperty()
    description = ndb.StringProperty()
    image_url = ndb.StringProperty()
