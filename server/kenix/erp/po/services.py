import endpoints
from protorpc import remote

from models import PoModel, PoLineModel
from kenix.erp.api import kenix_erp_api

@kenix_erp_api.api_class(resource_name='po')
class PurchaseOrderService(remote.Service):
    """
    Purchase Order API v1
    """

    @PoModel.query_method(path='po', name='index')
    def index(self, query):
        """
        List of purchase orders
        """
        return query

    @PoModel.method(request_fields=('id',), path='po/{id}', http_method='GET', name='get')
    def get(self, po_model):
        """
        Get a purchase order
        """
        if not po_model.from_datastore:
            raise endpoints.NotFoundException('PO not found.')
        return po_model

    @PoModel.method(path='po', http_method='POST', name='create')
    def create(self, po_model):
        """
        Place a new purchase order
        """
        po_model.put()
        return po_model

    @PoLineModel.method(path='po/{parent}', http_method='POST', name='line.create')
    def create_line(self, po_line_model):
        """
        Create a line of item for a purchase order
        """
        if po_line_model.from_datastore:
            raise endpoints.BadRequestException(
                'MyModel %s with parent %s already exists.' %
                (po_line_model.id, po_line_model.parent))
        po_line_model.put()
        return po_line_model


    @PoLineModel.query_method(query_fields=('parent',), path='po/{parent}', name='line.index')
    def index_line(self, query):
        """
        Line of items of a purchase order
        """
        return query

