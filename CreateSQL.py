import sqlite3
from Tables import product, Location
con = sqlite3.connect('FlaskInventory.db')

c= con.cursor()

c.execute("create table IF NOT EXISTS Product (prod_id INTEGER PRIMARY KEY AUTOINCREMENT,prod_name TEXT UNIQUE NOT NULL, prod_qty INTEGER NOT NULL )")  


c.execute("create table IF NOT EXISTS Location (loc_id INTEGER PRIMARY KEY AUTOINCREMENT, loc_name TEXT NOT NULL)")  


c.execute("create table IF NOT EXISTS ProductMovement (movement_id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT NOT NULL, from_location TEXT , to_location TEXT ,product_id INTEGER UNIQUE NOT NULL,pqty INTEGER NOT NULL)")  



c.execute("create table IF NOT EXISTS ProductBalance (balance_id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT NOT NULL, warehouse TEXT  NOT NULL, quantity INTEGER NOT NULL)")  


 
def insertProduct(prod):
    with con:
        c.execute("INSERT INTO Product VALUES (:prod_id,:prod_name,:prod_qty)",{'prod_id':prod.prod_id,'prod_name':prod.prod_name,'prod_qty':prod.prod_qty})


def printProduct():
    with  con:
         c.execute("SELECT * FROM ProductBalance")
         return c.fetchall()

def updateProduct(prod,prod_name):
    with con:
        c.execute("""UPDATE Product SET prod_name = :prod_name WHERE prod_qty = :prod_qty """,{'prod_id':prod.prod_id,'prod_name':prod_name,'prod_qty':prod.prod_qty})


def removeProduct(prod):
    with con:
        c.execute("DELETE from Product WHERE prod_name= :prod_name",{'prod_name':prod.prod_name})


#c.execute("SELECT try_name FROM TRY as t  INNER JOIN Product as p ON t.try_name=p.prod_name")  

#c.execute("INSERT INTO ProductBalance SELECT prod_id,prod_name,prod_qty,loc_name FROM Product, Location")


#c.execute('select * from ProductBalance')
#c.execute("Update ProductBalance set warehouse=(select prod_name from Product where Product.prod_name=ProductBalance.warehouse)")
#c.execute(''' UPDATE ProductBalance SET  warehouse  = ? select prod_name from Product''', (product.prod_name))


con.close()