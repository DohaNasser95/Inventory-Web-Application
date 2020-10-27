class Location:
   

    def __init__(self,loc_id,loc_name):
        self.loc_id=loc_id
        self.loc_name=loc_name


class product:
   
    def __init__(self,prod_id,prod_name,prod_qty):
        self.prod_id=prod_id
        self.prod_name=prod_name
        self.prod_qty=prod_qty


class ProductMovement:

    def __init__(self,movement_id,timestamp,from_location,to_location,product_id,pqty):
        self.movement_id=movement_id
        self.timestamp=timestamp
        self.from_location=from_location
        self.to_location=to_location
        self.product_id=product_id
        self.pqty=pqty

class ProductBalance:
    def __init__(self,balance_id,product,warehouse,quantity):
        self.balance_id=balance_id
        self.product=product
        self.warehouse=warehouse
        self.quantity=quantity
  