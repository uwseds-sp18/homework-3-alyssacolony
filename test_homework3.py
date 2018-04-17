import homework3 as hw
import sqlite3
from sqlite3 import OperationalError
import pandas as pd
import os
import unittest



print("Unit tests to validate that we have the right column names, all five languages are present, the DF has at least 10K rows, and that Id and Language are a key:")
df = hw.create_dataframe('Data-Essentials/class.db')

class UnitTests(unittest.TestCase):
	# df = hw.create_dataframe('Data-Essentials/class.db')
	# columns = list(df)
	def test_ColNames(self):
		self.assertEqual(set(list(df)), set(['video_id', 'category_id', 'language']))
	
	def test_LanguagesPresent(self):
		self.assertEqual(set(df.language.unique()), set(['FR', 'DE', 'GB', 'CA', 'US']))
	
	def test_DataFrameSize(self):
		self.assertTrue(df.shape[0] >10000)

	def test_IdLanIsKey(self):
		self.assertTrue(len(df[['video_id', 'language']].drop_duplicates()) == len(df.drop_duplicates()))
 
suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)


print("Edge test to see if correct exception (assignment defined \"ValueError\" as the correct exception) is generated when an invalid path is provided")
paths = ['mybadpath',
        3,
        [3,4,"five"]]

for path in paths:
    try:
        hw.create_dataframe(path)
    except ValueError:
        print("%s raised a value error" % str(path))
    except:
        print("%s raised a different type of error" % str(path))