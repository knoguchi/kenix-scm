import endpoints
from protorpc import remote
from models import InvModel
from kenix.erp.api import kenix_erp_api

@kenix_erp_api.api_class(resource_name='inventory')
class InvService(remote.Service):
    """
    Inventory API v1
    """

    @InvModel.query_method(path='inventory', name='index')
    def index(self, query):
        """
        List of book inventories
        """
        return query

    @InvModel.method(request_fields=('id',), path='inventory/{id}', http_method='GET', name='get')
    def get(self, inventory):
        """
        Get book inventories by SKU
        """
        if not inventory.from_datastore:
            raise endpoints.NotFoundException('Book inventory not found.')
        return inventory

    @InvModel.method(path='inventory', name='create')
    def create(self, inventory):
        """
        Createa a book inventory
        """
        # do some validation
        inventory.put()
        return inventory

    @InvModel.method(path='inventory/{id}', http_method='PUT', name='update')
    def update(self, inventory):
        """
        Update a book inventory
        """
        if not inventory.from_datastore:
            raise endpoints.NotFoundException('Book inventory not found')
        inventory.put()
        return inventory
