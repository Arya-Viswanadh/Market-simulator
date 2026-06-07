"""
Simple Market Simulator

Features:
- Order matching engine
- Trade execution
- Portfolio tracking
- P&L calculation
- Average buy price
- Trade statistics
"""
## Represents a buy or a sell order
class Order:
    def __init__(self, price, quantity, side):
        self.price = price
        self.quantity = quantity
        self.side = side
        
        

##stores orders and matches trades
class Orderbook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
        self.trades = []

    def add_order(self, order):
        if order.side == "buy":
            self.buy_orders.append(order)
        else:
            self.sell_orders.append(order)

    def match(self,trader):
        while self.buy_orders and self.sell_orders:

            best_buy = max(self.buy_orders, key=lambda x: x.price)
            best_sell = min(self.sell_orders, key=lambda x: x.price)

            if best_buy.price < best_sell.price:
                break

            trade_qty = min(best_buy.quantity, best_sell.quantity)
            trade_price= best_sell.price
            cost = trade_qty * trade_price
            

            if trader.cash < cost:
              print("INSUFFICIENT CASH")
              break

            trader.cash -= cost
            trader.position += trade_qty
            trader.total_cost += cost

            print("TRADE:", trade_qty, "at", trade_price)
            self.trades.append((trade_qty, trade_price))
          

            best_buy.quantity -= trade_qty
            best_sell.quantity -= trade_qty

            if best_buy.quantity == 0:
                self.buy_orders.remove(best_buy)

            if best_sell.quantity == 0:
                self.sell_orders.remove(best_sell)
                
    def show_book(self):
     print("\nBUY ORDERS:")
     for o in self.buy_orders:
        print(o.price, o.quantity)

     print("\nSELL ORDERS:")
     for o in self.sell_orders:
        print(o.price, o.quantity)
    def show_trades(self):
     print("\nTRADE HISTORY:")
     for qty, price in self.trades:
        print(qty, "at", price)

## tracks cash, positions and performances
class Trader:
    def __init__(self, cash):
        self.cash = cash
        self.position = 0
        self.total_cost = 0
    def pnl(self, current_price):
     return self.cash + self.position * current_price
    def average_price(self):
        if self.position == 0:
            return 0
        return self.total_cost / self.position
     
     



trader = Trader(1000)

# TEST
book = Orderbook()
import random

for i in range(5):

    price = random.randint(95, 105)
    qty = random.randint(1, 5)

    book.add_order(Order(price, qty, "buy"))

    price = random.randint(95, 105)
    qty = random.randint(1, 5)

    book.add_order(Order(price, qty, "sell"))

print("\nBEFORE MATCHING")
book.show_book()

book.match(trader)

print("\nAFTER MATCHING")
book.show_book()

book.show_trades()

market_price = random.randint(95, 105)

print("Market Price:", market_price)
print("P&L:", trader.pnl(market_price))

print("\n--- PORTFOLIO ---")
print("Cash:", trader.cash)
print("Shares:", trader.position)
print("Portfolio Value:", trader.pnl(market_price))
print("Average Buy Price:", trader.average_price())
print("Total Trades:", len(book.trades))
print("Total Volume:", sum(qty for qty, _ in book.trades))













