import logging
import pandas as pd
from tqdm import tqdm
from database import Database

logging.getLogger().setLevel(logging.INFO)

db = Database()
logging.info("Creating the corpora table...")
db.execute("""
           CREATE TABLE corpora
           (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           lang TEXT NOT NULL,
           texts_number INTEGER NOT NULL,
           tokens_number INTEGER NOT NULL,
           texts_number INTEGER NOT NULL);
           """)
logging.info("Table creation finished.")
