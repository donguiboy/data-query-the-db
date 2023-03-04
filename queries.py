# pylint:disable=C0111,C0103
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
datab = conn.cursor()

def query_orders(db):#DONE
    # return a list of orders displaying each column
    query = """select* from Orders o"""
    db.execute(query)
    results = db.fetchall()
    return results

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query= """select *
    from Orders o
    where OrderDate > ?
    and OrderDate <= ?
    """
    db.execute(query,(date_from,date_to))
    results = db.fetchall()
    return results

def get_waiting_time(db):
    query="""select *, (julianday(ShippedDate) - julianday(OrderDate)) AS TimeDelta
    from Orders
    order by TimeDelta ASC"""
    db.execute(query)
    results = db.fetchall()
    return results
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
