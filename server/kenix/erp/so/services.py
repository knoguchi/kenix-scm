import endpoints
from protorpc import remote

from models import SoModel, SoLineModel
from kenix.erp.api import kenix_erp_api

@kenix_erp_api.api_class(resource_name='so')
class SalesOrderService(remote.Service):
    """
    Purchase Order API v1
    """

    @SoModel.query_method(path='so', name='index')
    def index(self, query):
        """
        List of purchase orders
        """
        return query

    @SoModel.method(request_fields=('id',), path='so/{id}', http_method='GET', name='get')
    def get(self, so):
        """
        Get a purchase order
        """
        if not so.from_datastore:
            raise endpoints.NotFoundException('Sales Order not found.')
        return so

    @SoModel.method(path='so', http_method='POST', name='create')
    def create(self, so):
        """
        Post a new sales order
        """
        so.put()
        return so

    @SoLineModel.method(path='so/{parent}', http_method='POST', name='line.create')
    def create_line(self, so_line):
        """
        Create a line of item for a purchase order
        """
        if so_line.from_datastore:
            raise endpoints.BadRequestException(
                'MyModel %s with parent %s already exists.' %
                (so_line.id, so_line.parent))
        so_line.put()
        return so_line


    @SoLineModel.query_method(query_fields=('parent',), path='so/{parent}', name='line.index')
    def index_line(self, query):
        """
        Line of items of a purchase order
        """
        return query

