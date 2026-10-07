class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
        self.trades = []

    def add_order(self,order):
        if order.side == "BUY":
            self.buy_orders.append(order)
            self.buy_orders.sort(key= lambda order: (-order.price,order.timestamp))
        else:
            self.sell_orders.append(order)
            self.sell_orders.sort(key= lambda order: (order.price,order.timestamp))


    def match_orders(self):

        updated_orders = []
        updated_trades = []

        while self.buy_orders and self.sell_orders:

            matched = False

            # Check BUY orders according to priority
            for buy_order in list(self.buy_orders):

                matching_sell = None

                # Find the first SELL order for the same symbol
                for sell_order in self.sell_orders:
                    if sell_order.symbol == buy_order.symbol:
                        matching_sell = sell_order
                        break

                # No SELL order with the same symbol
                if matching_sell is None:
                    continue

                # BUY price must be greater than or equal to SELL price
                if buy_order.price < matching_sell.price:
                    continue

                # Determine trade quantity
                trade_quantity = min(
                    buy_order.quantity,
                    matching_sell.quantity
                )

                # Trade happens at BUY price
                trade_price = buy_order.price

                # Reduce remaining quantities
                buy_order.quantity -= trade_quantity
                matching_sell.quantity -= trade_quantity

                # Update BUY status
                if buy_order.quantity == 0:
                    buy_order.status = "FILLED"
                else:
                    buy_order.status = "PARTIALLY_FILLED"

                # Update SELL status
                if matching_sell.quantity == 0:
                    matching_sell.status = "FILLED"
                else:
                    matching_sell.status = "PARTIALLY_FILLED"

                # Store updated orders
                updated_orders.append(buy_order)
                updated_orders.append(matching_sell)

                # Create trade
                trade = {
                    "buy_order_id": buy_order.order_id,
                    "sell_order_id": matching_sell.order_id,
                    "quantity": trade_quantity,
                    "price": trade_price
                }

                self.trades.append(trade)
                updated_trades.append(trade)

                # Remove completely filled BUY
                if buy_order.quantity == 0:
                    self.buy_orders.remove(buy_order)

                # Remove completely filled SELL
                if matching_sell.quantity == 0:
                    self.sell_orders.remove(matching_sell)

                # A trade happened
                matched = True

                # Start checking from the highest-priority BUY again.
                # This allows a partially filled BUY to match another SELL.
                break

            # No trade was possible
            if not matched:
                break

        return updated_orders, updated_trades



    def display_order_book(self):
        print("========== ORDER BOOK =========")
        print()
        print("BUY ORDERS")
        print("Order ID | User | Symbol   | Quantity | Price")

        if self.buy_orders:
            for order in self.buy_orders:
                print(f"{order.order_id}      | {order.user_id}    | {order.symbol} | {order.quantity}     | {order.price}  ")
        else:
            print("no buy orders")
        print()

        print("SELL ORDERS")
        print("Order ID | User | Symbol   | Quantity | Price")
        if self.sell_orders:
            for order in self.sell_orders:
                print(f"{order.order_id}      | {order.user_id}    | {order.symbol} | {order.quantity}   | {order.price}  ")
        else:
            print("no sell orders")


    def display_trades(self):
        print("=====  ====== TRADE HISTORY ==========")
        print()
        print(f"Buy Order | Sell Order | Quantity | Price")

        if self.trades:
            for trade in self.trades:
                print(f"{trade['buy_order_id']} | {trade['sell_order_id']} | {trade['quantity']} | {trade['price']}")
        else:
            print("No Trades")
    