from kenix.erp.po.services import PurchaseOrderService
from kenix.erp.so.services import SalesOrderService
from kenix.erp.inventory.services import InvService
from kenix.erp.products.services import ProductService

services = [
    PurchaseOrderService,
    SalesOrderService,
    ProductService,
    InvService,
]