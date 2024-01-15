#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_count = 0
    self.last_total = 0

  def add_item(self, name, price, count=1):
    for i in range(count):
      self.items.append(name)
    self.last_count = count
    self.last_total = price * count
    self.total += self.last_total


  def apply_discount(self):
    if self.discount != 0:
      self.total -= self.total * (self.discount / 100)
      self.last_total -= self.last_total * (self.discount / 100)
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print('There is no discount to apply.')

  def reset_register_totals(self):
    self.total = 0
    self.items = []
    self.last_count = 0
    self.last_total = 0

  def void_last_transaction(self):
    self.total -= self.last_total
    for i in range(self.last_count):
      self.items.pop()

  
