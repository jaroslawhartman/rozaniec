#!/usr/bin/env python

from datetime import date
from socket import *
import os
import time
import random

# Data

mysteries = { 
	'Radosna' : [
        'Zwiastowanie Najswietszej Maryi Pannie',
        'Nawiedzenie swietej Elzbiety',
        'Narodzenie Jezusa',
        'Ofiarowanie Jezusa w swiatyni',
        'Odnalezienie Jezusa w swiatyni'
	],

	'Bolesna' : [
        'Modlitwa Jezusa w Ogrojcu',
        'Biczowanie Jezusa',
        'Cierniem ukoronowanie Jezusa',
        'Dzwiganie krzyza na Kalwarie',
        'Ukrzyzowanie i smierc Jezusa'
	],

	'Chwalebna' : [
        'Zmartwychwstanie Jezusa Chrystusa',
        'Wniebowstapienie Chrystusa',
        'Zeslanie Ducha Swietego',
        'Wniebowziecie Najswietszej Maryi Panny',
        'Ukoronowanie Maryi na Krolowa nieba i ziemi'
	],

	'Swiatla' : [
        'Chrzest Jezusa w Jordanie',
        'Objawienie sie Jezusa w Kanie Galilejskiej',
        'Gloszenie krolestwa i wzywanie do nawrocenia',
        'Przemienienie Panskie na gorze Tabor',
        'Ustanowienie Eucharystii'
	]
}

class Rosarist:

	def find_mysterytype(self):
		today = date.weekday(date.today())

		if (today in (0,5)): return 'Radosna'
		if (today in (1,4)): return 'Bolesna'
		if (today in (2,6)): return 'Chwalebna'
		if (today == 3):     return 'Swiatla'

	def find_mystery(self, decade, mysterytype):
		return mysteries[mysterytype][decade]

	def mystery_for_today(self):
	    decate = random.randint(0, 4)
	    mysterytype = self.find_mysterytype()
	    mystery = self.find_mystery(decate, mysterytype)
	    print "Tajemnica {0} - {1}".format(mysterytype, mystery)

if __name__ == "__main__":
	rosarist = Rosarist()
	rosarist.mystery_for_today()