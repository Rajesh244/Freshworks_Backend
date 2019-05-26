# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:30:45 2019

@author: Rajesh
"""
import unittest,os
from Database import Database
 
class UnitTest(unittest.TestCase):
 
    def setUp(self):
        self.db=Database("Test")
        self.db_loc=Database("Test_loc","F:\Freshworkks\Database")
        
    def create(self):       
        self.assertEqual(os.path.isfile(os.path.join("F:\Freshworkks\Database",self.db_loc+".json")),True,"File Not created")
        self.assertEqual(os.path.isfile(os.path.join(os.getcwd(),self.db+".json")),True,"File Not created")
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)