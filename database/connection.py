import mysql.connector
from models.order import Order
from orderbook.order_book import OrderBook

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "albin003",
    database = "EquiMatch_db"
)

if connection.is_connected():
    print("Connected Successfully!")
else:
    print("Connection Failed")


cursor = connection.cursor()

# -----insert data's into users table --------

# cursor.execute("""INSERT INTO users (user_name,email,password)
#         VALUES ("Albin","albin@gmail.com","albin123"),
#         ("Rahul","rahul@gmail.com","rahul123"),
#         ("Anu","anu@gmail.com","anu123"),
#         ("Arjun","arjun@gmail.com","arjun123")
#     """)

# connection.commit()

# cursor.execute(""" SELECT * FROM users """)
# for data in cursor.fetchall():
#     print(data)


# cursor.execute(""" ALTER TABLE orders  MODIFY COLUMN timestamp DATETIME""")
# connection.commit()

#----------insert data's into orders table --------

# cursor.execute("""INSERT INTO orders (user_id,symbol,side,quantity,price,timestamp)
#         VALUES (1,"RELIANCE","BUY",100,1400,"2026-09-25 10:30:00"),(2,"RELIANCE","BUY",50,1395,"2026-09-25 10:30:25"),
#         (3,"RELIANCE","SELL",100,1400,"2026-09-25 11:15:11"),(4,"RELIANCE","SELL",100,1405,"2026-09-25 11:45:12"),
#         (1,"RELIANCE","BUY",60,1400,"2026-09-25 10:20:00"),(2,"RELIANCE","BUY",60,1400,"2026-09-25 10:20:05")
# """)

# connection.commit()

# orderbook = OrderBook()
# cursor.execute(""" SELECT * FROM orders """)
# for data in cursor.fetchall():
#     order = Order(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
    
#     orderbook.add_order(order)


# cursor.execute(""" UPDATE orders SET quantity = %s, status = %s WHERE order_id = %s """,(best_buy.quantity,best_buy.status,best_buy.order_id))
# cursor.execute(""" UPDATE orders SET quantity = %s, status = %s WHERE order_id = %s """,(best_sell.quantity,best_sell.status,best_sell.order_id))
# connection.commit()


# cursor.execute("""SELECT * FROM orders WHERE (status = "PARTIALLY_FILLED" OR status = "PENDING")""")







