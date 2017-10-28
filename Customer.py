#!/usr/bin/python

class Customer:

	def __init__(self, name, surname, ticketPrice):
		self.name = name
		self.surname = surname
		self.ticketPrice = ticketPrice

	def __str__(self):
		return '%s %s %d' % (self.name, self.surname, self.ticketPrice)
