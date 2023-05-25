#!/usr/bin/env python3

class CashRegister:
      def __init__(self, discount=0):
            self.discount = discount
            self.total = 0
            self.items = []
            self.last_transaction = []
            
      def add_item(self, title, price, quantity=1):
            # self.price = price
            self.title = title
            self.total += (price * quantity)
            self.items.extend([title]*quantity)
            self.last_transaction = [{ 'title' : title , 'quantity' : quantity, "price" : price}]
            # for counter in range(quantity):
            #   self.items.append(title)

# for x in range(start, end right before this, step by)
# for (let x=50;x<=60;x+2)

      def apply_discount(self):
            # lets pseudocode this
            # return total * discount 
            # total = price * quantity   discount = 20
            if self.discount > 0 :
              self.total = self.total - (self.total * (self.discount/ 100)) 
              print(f'After the discount, the total comes to ${int(self.total)}.')
            else: 
                 print('There is no discount to apply.')
                #  add_item(tomato, 1.76, 3)

# self.items=['eggs','tomato','eggs']
# self.last_transaction=[]

      def void_last_transaction(self):
          #  void, quantity, total, title
          #  delete, remove, pop from items 

          # updated total
          self.total = self.total - (self.last_transaction[0]['price'] * self.last_transaction[0]['quantity'])
          # updated items
          for x in range(self.last_transaction[0]['quantity']):
            self.items.pop()
          # updated last_transaction
          self.last_transaction.pop()
          
                
            
                



