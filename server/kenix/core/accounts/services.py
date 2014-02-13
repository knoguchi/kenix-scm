from protorpc import remote
import endpoints

from kenix.core.api import kenix_core_api
from models import AccountModel


@kenix_core_api.api_class(resource_name='accounts')
class AccountService(remote.Service):
    """
    Account Service v1
    """

    @AccountModel.query_method(path='accounts', name='index')
    def index(self, query):
        """
        List of accounts
        """
        return query

    @AccountModel.method(path='accounts/{id}', http_method='GET', name='get')
    def get(self, account):
        """
        Get an account
        """
        if not account.from_datastore:
            raise endpoints.NotFoundException('User not found')
        return account

    @AccountModel.method(path='accounts', name='create')
    def create(self, account):
        """
        Createa an account
        """
        # do some validation
        account.put()
        return account

    @AccountModel.method(path='accounts/{id}', http_method='PUT', name='update')
    def update(self, account):
        """
        Update an account
        """
        if not account.from_datastore:
            raise endpoints.NotFoundException('User not found')
        account.put()
        return account
