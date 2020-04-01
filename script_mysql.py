import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mypythondb"
)

mycursor = mydb.cursor()

###################################################
################### INSERT  #######################
###################################################

def insert():
    mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), address VARCHAR(255));")
    #mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
    ]

    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    for x in mycursor:
        print(x)


############# SELECT ###################

def select():
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


############  SELECT ONE ####################
def select_one():
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchone()
    print(myresult)

############  SELECT WHERE  ####################
def select_where():
    sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)



def select_orderby():
    sql = "SELECT * FROM customers ORDER BY name"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

################################################
########### SELECT ORDER BY DESCENDING #########
################################################
def select_orderby_desc():
    sql = "SELECT * FROM customers ORDER BY name DESC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

################################################
###############    DELETE     ##################
################################################
def delete():
    sql = "DELETE FROM customers WHERE address = 'Mountain 21'" 
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")



####The mysql.connector module uses the placeholder %s to escape values in the delete statement:
################################################
###############    DELETE BY ADDRESS    ##################
################################################
def delete_by_address(address="Yellow Garden 2"):
    sql = "DELETE FROM customers WHERE address = %s"
    adr = (address,)
    mycursor.execute(sql, adr)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")


################################################
###############    UPDATE   ##################
################################################
def update():
    sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")


def update_by_address(oldaddress="Valley 345", newaddress="Canyon 123"):
    sql = "UPDATE customers SET address = %s WHERE address = %s"
    val = (oldaddress,newaddress)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")


def select_with_limit():
    mycursor.execute("SELECT * FROM customers LIMIT 5")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

########################
#######  If you want to return five records, 
# starting from the third record, you can use the "OFFSET" keyword:
########################################

def select_with_limit_offset():
    mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


############  JOIN TWO DATABASES #####################

def join():
    sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)






# insert()
# select()
# select_one()
# select_where()
# select_orderby()
# select_orderby_desc()
# delete_by_address()
# update()
# update_by_address()
# select_with_limit()
select_with_limit_offset()
mydb.close()


# mycursor.execute("DROP TABLE store")
# mycursor.execute("DROP TABLE IF EXISTS store")
# mycursor.execute("CREATE TABLE IF NOT EXISTS store (id INT AUTO_INCREMENT PRIMARY KEY, item TEXT, quantity INT, price REAL);")
# sql = "INSERT INTO store (item, quantity, price) VALUES (%s,%s, %s)"
# val = ("Whiskey", 5,2)
# mycursor.execute(sql, val)

#mydb.commit()

#mycursor.execute("SHOW TABLES")

# mycursor.execute("CREATE DATABASE IF NOT EXISTS mypythondb")
# mycursor.execute("SHOW DATABASES")

