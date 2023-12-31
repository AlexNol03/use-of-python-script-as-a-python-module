# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:34:03 2023

@author: Alex Nolan
"""
import numpy as np
import LoanPayments as ls
PV = 1000
r = 5
n = 12
pmt = ls.computesPmt(PV, r, n)
print(f"pmt = {pmt}")

pmt2 = ls.computesPmt(1000, 5, 12)
print(f"and the pmt also is {pmt2}")