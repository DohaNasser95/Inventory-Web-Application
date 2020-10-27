from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
import sqlite3
from Tables import product, Location, ProductBalance,ProductMovement
import CreateSQL



app = Flask(__name__)



@app.route('/')
def header():
    return render_template('header.html')
@app.route('/overview.html')
def overview():
    con = sqlite3.connect("FlaskInventory.db")  
    con.row_factory = sqlite3.Row 
    cur = con.cursor()  
   
    #cur.execute("INSERT INTO TRY SELECT prod_id,prod_name FROM Product")
    #cur.execute("SELECT product FROM ProductBalance  INNER JOIN Product  ON ProductBalance.product=Product.prod_name")
    cur.execute("select * from ProductBalance")  
    contacts =cur.fetchall()
    return render_template('overview.html', contacts=contacts)

@app.route('/product.html')
def product():
    con = sqlite3.connect("FlaskInventory.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Product")  
    rows = cur.fetchall()  
    return render_template("product.html",rows = rows)

@app.route('/location.html')
def location():
    con = sqlite3.connect("FlaskInventory.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Location")  
    rows = cur.fetchall()  
    return render_template('location.html',rows = rows)

@app.route('/productMovement.html')
def productMovement():
    con = sqlite3.connect("FlaskInventory.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from ProductMovement")  
    rows = cur.fetchall()  
    return render_template('productMovement.html',rows = rows)


@app.route('/insert',methods=["POST"])
def insert():
    msg="msg"
    if request.method == "POST":
        try:
             prod_name = request.form["name"]
             prod_qty=request.form["Qty"]
             with sqlite3.connect("FlaskInventory.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Product (prod_name,prod_qty) values (?,?)",(prod_name,prod_qty))  
                con.commit()  
                msg = "Product successfully Added"
        except:  
            con.rollback()  
            msg = "We can not add the product to the list, Please enter a unique id" 
        finally:  
            return render_template("success.html",msg = msg)  
            con.close() 


@app.route('/insertLoc',methods=["POST"])
def insertLoc():
    msg="msg"
    if request.method == "POST":
        try:
             loc_id=request.form["id"]
             loc_name = request.form["name"]
             with sqlite3.connect("FlaskInventory.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Location (loc_id,loc_name) values (?,?)",(loc_id,loc_name))  
                con.commit()  
                msg = "Location successfully Added"
        except:  
            con.rollback()  
            msg = "We can not add the location to the list,Please enter a unique id" 
        finally:  
            return render_template("success.html",msg = msg)  
            con.close() 


@app.route('/Move',methods=["POST"])
def Move():
    msg="msg"
    if request.method == "POST":
        try:
             timestamp = request.form["ts"]
             from_location  = request.form["from_loc"]
             to_location  = request.form["to_loc"]
             product_id  = request.form["p_id"]
             pqty  = request.form["qty"]
             with sqlite3.connect("FlaskInventory.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into ProductMovement (timestamp,from_location,to_location,product_id,pqty) values (?,?,?,?,?)",(timestamp,from_location,to_location,product_id,pqty))  
                con.commit()  
                msg = "Move Product successfully Added"
        except:  
            con.rollback()  
            msg = "We can not move product to the list,Please enter a unique id" 
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()



@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["Did"]  
    with sqlite3.connect("FlaskInventory.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Product where prod_id = ?",id)  
            msg = "record successfully deleted" 
        except:  
            msg = "can't be deleted" 
        finally:  
            return render_template("success.html",msg = msg)


@app.route("/deleterecordLoc",methods = ["POST"])  
def deleterecordLoc():  
    id = request.form["Did"]  
    with sqlite3.connect("FlaskInventory.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Location where loc_id = ?",id)  
            msg = "record successfully deleted" 
        except:  
            msg = "can't be deleted" 
        finally:  
            return render_template("success.html",msg = msg)

@app.route("/deleterecord2",methods = ["POST"])  
def deleterecord2():  
    id = request.form["id"]  
    with sqlite3.connect("FlaskInventory.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from ProductMovement where movement_id = ?",id)  
            msg = "record successfully deleted" 
        except:  
            msg = "can't be deleted" 
        finally:  
            return render_template("success.html",msg = msg)


@app.route("/updateProduct",methods = ["POST"])  
def updateProduct():  
    prod_name = request.form["prodname"]
    prod_qty=request.form["prodQty"]
    with sqlite3.connect("FlaskInventory.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("UPDATE Product SET prod_name = ?, prod_qty = ?",(prod_name, prod_qty))  
            msg = "record successfully updated" 
        except:  
            msg = "can't be updated" 
        finally:  
            return render_template("success.html",msg = msg)

@app.route("/updateLocation",methods = ["POST"])  
def updateLocation():  
    loc_id=request.form["locid"]
    loc_name=request.form["locname"]
    with sqlite3.connect("FlaskInventory.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("UPDATE Location SET loc_id = ?, loc_name = ?",(loc_id,loc_name))  
            msg = "record successfully updated" 
        except:  
            msg = "can't be updated" 
        finally:  
            return render_template("success.html",msg = msg)
  
@app.route("/updateProductMove",methods = ["POST"])  
def updateProductMove():  
    timestamp = request.form["ts"]
    from_location  = request.form["from_loc"]
    to_location  = request.form["to_loc"]
    product_id  = request.form["p_id"]
    pqty  = request.form["qty"]
    with sqlite3.connect("FlaskInventory.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("UPDATE ProductMovement SET timestamp = ?,from_location = ?, to_location = ?, product_id = ?, pqty = ?",(timestamp,from_location,to_location,product_id,pqty))  
            msg = "record successfully updated" 
        except:  
            msg = "can't be updated" 
        finally:  
            return render_template("success.html",msg = msg)

@app.route("/viewProduct.html")  
def viewProduct():  
    con = sqlite3.connect("FlaskInventory.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Product")  
    rows = cur.fetchall()  
    return render_template("viewProduct.html",rows = rows)

@app.route("/viewLocation.html")  
def viewLocation():  
    con = sqlite3.connect("FlaskInventory.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Location")  
    rows = cur.fetchall()  
    return render_template("viewLocation.html",rows = rows)   

@app.route("/viewProductMov.html")  
def viewProductMov():  
    con = sqlite3.connect("FlaskInventory.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from ProductMovement")  
    rows = cur.fetchall()  
    return render_template("viewProductMov.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)