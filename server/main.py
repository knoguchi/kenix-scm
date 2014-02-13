import endpoints
from kenix.core import services as core_services
from kenix.erp import services as erp_services
from kenix.wms import services as wms_services

all_services = core_services + erp_services + wms_services
application = endpoints.api_server(all_services, restricted=False)

