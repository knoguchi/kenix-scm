import endpoints
from protorpc import remote
from models import ProductModel
from kenix.erp.api import kenix_erp_api

@kenix_erp_api.api_class(resource_name='products')
class ProductService(remote.Service):
    """
    Product API v1
    """

    @ProductModel.query_method(path='products', name='index')
    def index(self, query):
        """
        List of on-hand inventories
        """
        return query

    @ProductModel.method(request_fields=('id',), path='products/{id}', http_method='GET', name='get')
    def get(self, product):
        """
        Get product
        """
        if not product.from_datastore:
            raise endpoints.NotFoundException('Product not found.')
        return product

    @ProductModel.method(path='products', name='create')
    def create(self, product):
        """
        Createa a product
        """
        # do some validation
        product.put()
        return product

    @ProductModel.method(path='product/{id}', http_method='PUT', name='update')
    def update(self, product):
        """
        Update a product
        """
        if not product.from_datastore:
            raise endpoints.NotFoundException('Product not found')
        product.put()
        return product
