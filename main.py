from models.order import Order
from orderbook.order_book import OrderBook
from database.connection import connection,cursor


user_email = input("Enter the Email : ")
user_password = input("Enter the Password : ")

cursor.execute("""
        SELECT * FROM users WHERE email = %s AND password = %s
""",(user_email,user_password,))

existing_user = cursor.fetchone()
user_id = existing_user[0]
if existing_user:
    print(f"Login Successful\nUser ID : {user_id} \n User Name : {existing_user[1]}")

    while True:
        symbol = input("Enter the Stock : ")
        if symbol:
            symbol = symbol.upper()
            break
        else:
            print("---PLEASE ENTER STOCK----")

    while True:
        side = input("Enter BUY/SELL : ")
        if side == 'BUY' or side == 'SELL':
            side = side
            break
        else:
            print("INVALID INPUT-----TRY AGIAN-----")

    while True:
        try:
            quantity = int(input("Enter the Quantity : "))

            if quantity > 0:
                quantity = quantity
                break
            else:
                print("INVALID INPUT----TRY AGAIN---- ")
        except ValueError:
            print("Invalid input. Please enter a number.")


    while True:
        try:
            price = int(input("Enter the Price : "))
            if price > 0:
                price = price
                break
            else:
                print("INVALID INPUT----TRY AGAIN-----")
        except ValueError:
            print("Invalid input")

else:
    print("Unverified User")
    exit()

cursor.execute("""
    SELECT * FROM orders WHERE orders.user_id = %s
""",(user_id,))

order_history = cursor.fetchall()
print("Order_id | Symbol | Side | Quantity | Price | Status |")
for trade in order_history:
    print(f"{trade[0] }|{ trade[2]} | {trade[3]} | {trade[4]} | {trade[5]} | {trade[7]}")


cursor.execute("""
    INSERT INTO orders
    (user_id, symbol, side, quantity, price, timestamp, status)
    VALUES (%s, %s, %s, %s, %s, NOW(), %s)
""", (
    user_id,
    symbol,
    side,
    quantity,
    price,
    "PENDING"
))

connection.commit()

order_id = cursor.lastrowid
# print("New Order ID :", order_id)

cursor.execute("""
        SELECT * FROM orders WHERE order_id = %s
""",(order_id,))

new_order = cursor.fetchone()
# if new_order:
#     print("New order : ",new_order)
# else:   
#     print("not")


orderbook = OrderBook()

cursor.execute("""SELECT * FROM orders WHERE (status = "PARTIALLY_FILLED" OR status = "PENDING")""")
for data in cursor.fetchall():
    order = Order(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
    orderbook.add_order(order)


updated_orders,updated_trades = orderbook.match_orders()

for order in updated_orders:
    cursor.execute("""
            UPDATE orders SET quantity = %s, status = %s WHERE order_id = %s""",(order.quantity,order.status,order.order_id))
connection.commit()



for trade in updated_trades:

    cursor.execute("""
        INSERT INTO trades
        (buy_order_id, sell_order_id, quantity, price)
        VALUES (%s, %s, %s, %s)
    """, (
        trade["buy_order_id"],
        trade["sell_order_id"],
        trade["quantity"],
        trade["price"]
    ))

    print("=====TRADE=====")
    print(f"Buy Order : {trade['buy_order_id']}")
    print(f"Sell Order : {trade['sell_order_id']}")
    print(f"Quantity : {trade['quantity']}")
    print(f"Price : {trade['price']}")
    print("===============")

connection.commit()





orderbook.display_order_book()