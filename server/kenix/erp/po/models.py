import endpoints
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsAliasProperty
from endpoints_proto_datastore.ndb import EndpointsModel


class PoModel(EndpointsModel):
    po_num = ndb.StringProperty()
    order_date = ndb.DateProperty()
    status = ndb.StringProperty()
    bill_to = ndb.KeyProperty(kind='AddressModel')

    def line_of_items(self):
        """
        return line of items
        Ancestor query for strong consistency
        """
        q = PoLineModel.query(ancestor=self.key)
        return q.fetch()


class PoLineModel(EndpointsModel):
    """
    PO Line of Item.
    """
    _parent = None
    _id = None

    # header info
    po_key = ndb.KeyProperty(PoModel)
    po_num = ndb.StringProperty()
    order_date = ndb.DateProperty()

    # line info
    po_line_num = ndb.IntegerProperty()
    item = ndb.StringProperty()
    qty = ndb.IntegerProperty()
    description = ndb.StringProperty()
    price = ndb.FloatProperty()
    tax = ndb.FloatProperty()

    # line level ship-to 
    ship_to = ndb.KeyProperty(kind='AddressModel')
    ship_window_from = ndb.DateProperty()
    ship_window_to = ndb.DateProperty()

    # C: Collect, P: Prepaid, 3: Third party
    freight_term = ndb.StringProperty(choices=['C', 'P', '3'])
    # for prepaid carrier
    preferred_carrier = ndb.StringProperty()
    carrier_account = ndb.StringProperty()

    # partial fill info
    demand = ndb.IntegerProperty(default=1)
    schedule = ndb.IntegerProperty(default=1)
    # N: New, P: Partial, B: Back order, X: Canceled, C: Closed
    po_line_status = ndb.StringProperty(choices=['N', 'P', 'B', 'X', 'C'])

    def SetKey(self):
        """
        set key of the PoLineModel object that includes ancestor key from PoModel object
        """
        if self._parent is not None and self._id is not None:
            key = ndb.Key(PoModel, self._parent, PoLineModel, self._id)
            self.UpdateFromKey(key)

    def SetParts(self):
        if self.key is not None:
            parent_pair, id_pair = self.key.pairs()
            self._parent = parent_pair[1]
            self._id = id_pair[1]

    def ParentSet(self, value):
        if not isinstance(value, basestring):
            raise TypeError('PoModel name must be a string.')
        self._parent = value
        if ndb.Key(PoModel, value).get() is None:
            raise endpoints.NotFoundException('PoModel %s does not exist.' % value)
        self.SetKey()
        self._endpoints_query_info.ancestor = ndb.Key(PoModel, value)

    @EndpointsAliasProperty(setter=ParentSet, required=True)
    def parent(self):
        if self._parent is None:
            self.SetParts()
        return self._parent

    def IdSet(self, value):
        if not isinstance(value, basestring):
            raise TypeError('ID must be a string.')
        self._id = value
        self.SetKey()

    @EndpointsAliasProperty(setter=IdSet, required=True)
    def id(self):
        if self._id is None:
            self.SetParts()
            return self._id
