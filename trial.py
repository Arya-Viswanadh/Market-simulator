class Order:
    def __init__(self, price, quantity, side):
        self.price = price
        self.quantity = quantity
        self.side = side


class Orderbook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def add_order(self, order):
        if order.side == "buy":
            self.buy_orders.append(order)
        else:
            self.sell_orders.append(order)

    def match(self):
        if not self.buy_orders or not self.sell_orders:
            return

        best_buy = max(self.buy_orders, key=lambda x: x.price)
        best_sell = min(self.sell_orders, key=lambda x: x.price)

        if best_buy.price >= best_sell.price:
            trade_qty = min(best_buy.quantity, best_sell.quantity)

            print("TRADE:", trade_qty, "at", best_sell.price)

            best_buy.quantity -= trade_qty
            best_sell.quantity -= trade_qty

            if best_buy.quantity == 0:
                self.buy_orders.remove(best_buy)

            if best_sell.quantity == 0:
                self.sell_orders.remove(best_sell)


# ---------------- TEST ----------------

book = Orderbook()

book.add_order(Order(100, 5, "buy"))
book.add_order(Order(99, 3, "sell"))

book.match()

print(len(book.buy_orders))
print(len(book.sell_orders))