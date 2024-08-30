#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = (None, 0, 0)  
    
    def add_item(self, title, price, quantity=1):
        '''Accepts a title, a price, and an optional quantity.'''
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = (title, price, quantity)
    
    def apply_discount(self):
        '''Applies the discount to the total price.'''
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        '''Subtracts the last item from the total.'''
        title, price, quantity = self.last_transaction
        if title is not None:
            self.total -= price * quantity
            # Remove the item from the items list
            for _ in range(quantity):
                self.items.remove(title)
            # Reset the last_transaction to prevent further modifications
            self.last_transaction = (None, 0, 0)

