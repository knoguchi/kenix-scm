import endpoints
from protorpc import remote
from models import StockModel
from kenix.wms.api import kenix_wms_api

@kenix_wms_api.api_class(resource_name='stock')
class StockService(remote.Service):
    """
    Stock Inventory API v1
    """

    @StockModel.query_method(path='stock', name='index')
    def index(self, query):
        """
        List of stock inventories
        """
        return query

    @StockModel.method(request_fields=('id',), path='stock/{id}', http_method='GET', name='get')
    def get(self, stock):
        """
        Get stock inventories by SKU
        """
        if not stock.from_datastore:
            raise endpoints.NotFoundException('Stock inventory not found.')
        return stock

    @StockModel.method(path='stock', name='create')
    def create(self, stock):
        """
        Createa an stock inventory
        """
        # do some validation
        stock.put()
        return stock

    @StockModel.method(path='stock/{id}', http_method='PUT', name='update')
    def update(self, stock):
        """
        Update an stock inventory
        """
        if not stock.from_datastore:
            raise endpoints.NotFoundException('Stock invnetory not found')
        stock.put()
        return stock
