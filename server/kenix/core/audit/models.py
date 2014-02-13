from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel
from kenix.common.models import MoneyProperty


class ActivityModel(EndpointsModel):
    """
    Activity model class
    types:
        all: All Activity
        ship: Shipping Orders
        receive: Receiving Orders
        holds: Held Orders
        backorder: Backordered
        returns: Returns
        payments: Payments
        supportservices: Support Services
        projects: Special Projects
        pricing: Pricing
        adjustments: Billing Adjustments
        claims: Loss & Damage Claims

    attrs:
        description
        status
        items
        amount
        transaction id
        cart order#
        address1
        address2
        address3
        city
        state
        postal code
        country
        phone
        warehouse
        carrier
        tracking
        sku name
        sku description
        sku type
        sku qty
        sku cost
        sku retail
        submitted
        completed
        plan items
        shipping cost
        handling cost
        customer email
        customer name
        claim status
        good
        damaged
        sell tool name
        sell tool acct
        sell tool txn
    status:
        On Hold
        Completed

    """
    type = ndb.StringProperty()
    attrs = ndb.JsonProperty()
    created = ndb.DateTimeProperty(auto_now_add=True, auto_now=False)
    updated = ndb.DateTimeProperty(auto_now_add=True, auto_now=True)
