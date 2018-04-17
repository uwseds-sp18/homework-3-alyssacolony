import sqlite3
from sqlite3 import OperationalError
import pandas as pd
import os

def create_dataframe(databasePath):
    if not os.path.exists(str(databasePath)):
        raise ValueError("'{0}' is not a valid path".format(databasePath))
    else:
        conn = sqlite3.connect(databasePath)
        cur = conn.cursor()
        myTable = pd.read_sql_query("""
        select video_id, category_id, "CA" as language from CAvideos
        UNION 
        select video_id, category_id, "FR" as language from FRvideos
        UNION 
        select video_id, category_id, "US" as language from USvideos
        UNION 
        select video_id, category_id, "DE" as language from DEvideos
        UNION 
        select video_id, category_id, "GB" as language from GBvideos;""", conn)
        return(myTable)
    
    
