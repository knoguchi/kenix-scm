import endpoints
from protorpc import remote

from kenix.wms.models import RcvOrderModel
from kenix.wms.api import kenix_wms_api

@kenix_wms_api.api_class(resource_name='rcv_order')
class ReceivingOrderService(remote.Service):
    """
    Receiving Order API v1
    """

    @RcvOrderModel.query_method(path='rcv_orders', name='index')
    def index(self, query):
        """
        List of receiving orders
        """
        return query

    @RcvOrderModel.method(request_fields=('id',), path='rcv_orders/{id}', http_method='GET', name='get')
    def get(self, rcv_order):
        """
        Get a receiving order
        """
        if not rcv_order.from_datastore:
            raise endpoints.NotFoundException('Receiving Order not found.')
        return rcv_order

    @RcvOrderModel.method(path='rcv_orders', http_method='POST', name='create')
    def create(self, rcv_order):
        """
        Create a new receiving order
        """
        rcv_order.put()
        return rcv_order