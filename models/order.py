class Order:
    def __init__(self,order_id,user_id,symbol,side,quantity,price,timestamp,status):
        self.order_id = order_id
        self.user_id = user_id
        self.symbol = symbol
        self.side = side
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp
        self.status = status