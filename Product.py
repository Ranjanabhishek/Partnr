import requests
from Redis import redis
import json
from django.http import HttpResponse
import uuid

class ProductManage:
    def __init__(self, product_name, price, stock, category, user_id):
        self.user_id = user_id
        self.product_name = product_name
        self.price = price
        self.stock = stock
        self.category = category
        self.user_adding_product = {}
        self.product = {}
        self.response = {}

    def AddProduct(self):
        product_id = uuid()
        # as we created tables in models then we can also table to store data for ex:
        from models import ProductTable
        # self.product[product_id] = {self.product_name, self.price, self.stock}
        response = ProductTable.objects.create(name = self.product_name, price = self.price, category = self.category,\
                                stock = self.stock)
        
        self.user_adding_product[self.user_id] = product_id
        self.response['status'] = 200
        return HttpResponse(json.dumps(self.response), content_type="application/json")
    
    def ListAllproducts(self):
        product_list = list(self.user_adding_product.values())
        if product_list:
          return HttpResponse(json.dumps(product_list), content_type="application/json")
        else:
            return HttpResponse(json.dumps("No product found"), content_type="application/json")
    
    def UpdateProduct(self, product_id):
        product_details = self.product.get(product_id, None)
        if product_details:
            self.product.update({self.product_name, self.price, self.stock})
            return HttpResponse(json.dumps("product updates"), content_type="application/json")
        else:
            return HttpResponse(json.dumps("No product found"), content_type="application/json")
    
    def DeleteProduct(self, product_id):
        if self.product.get(product_id):
            self.product.pop(product_id)
            return HttpResponse(json.dumps("product deleted"), content_type="application/json")
        else:
            return HttpResponse(json.dumps("No product found"), content_type="application/json")
            


        




        
