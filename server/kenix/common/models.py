from decimal import Decimal
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel
from kenix.common.money import Money


class DecimalProperty(ndb.TextProperty):
    def _validate(self, value):
        if not isinstance(value, (Decimal, str)):
            raise ndb.datastore_errors.BadValueError('Expected decimal or string, got %r' % value)

        return Decimal(value)

    def _to_base_type(self, value):
        if not isinstance(value, (str, Decimal)):
            raise TypeError('DecimalProperty %s can only be set to string values; received %r' % (self._name, value))
        return str(value)

    def _from_base_type(self, value):
        try:
            return Decimal(value)
        except ValueError:
            return None


class MoneyProperty(ndb.TextProperty):
    def _validate(self, value):
        if not isinstance(value, (Money, str)):
            raise ndb.datastore_errors.BadValueError('Expected Money or string, got %r' % value)

        return Money(value)

    def _to_base_type(self, value):
        if not isinstance(value, (str, Money)):
            raise TypeError('MoneyProperty %s can only be set to string values; received %r' % (self._name, value))
        return str(value)

    def _from_base_type(self, value):
        try:
            return Money(value)
        except ValueError:
            return None


class BaseSerialNumberModel(EndpointsModel):
    """
    Serial number generator.

    """
class AddressModel(EndpointsModel):
    phone = ndb.StringProperty()
    addr1 = ndb.StringProperty()
    addr2 = ndb.StringProperty()
    addr3 = ndb.StringProperty()
    addr4 = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    zip1 = ndb.StringProperty()
    zip2 = ndb.StringProperty()
    country = ndb.StringProperty()


class ContactModel(EndpointsModel):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
