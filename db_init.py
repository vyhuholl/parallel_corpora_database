import logging
from database import Database

logging.getLogger().setLevel(logging.INFO)

db = Database()

logging.info("Creating the corpora table...")
db.execute("""
           CREATE TABLE corpora
           (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           lang TEXT NOT NULL,
           texts_number INTEGER NOT NULL,
           sents_number INTEGER NOT NULL,
           tokens_number INTEGER NOT NULL,
           tokens_percent FLOAT NOT NULL);
           """)
logging.info("Table creation finished.")

logging.info("Creating the texts table...")
db.execute("""
           CREATE TABLE texts
           (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           corpus_id INTEGER NOT NULL,
           author_id INTEGER,
           second_author_id INTEGER,
           translator_id INTEGER,
           second_translator_id INTEGER,
           name_original TEXT NOT NULL,
           name_translated TEXT,
           sphere TEXT NOT NULL,
           creation_date INTEGER,
           translation_date INTEGER,
           sents_number INTEGER NOT NULL,
           tokens_number INTEGER NOT NULL,
           );
           """)
logging.info("Table creation finished.")

logging.info("Creating the authors table...")
db.execute("""
           CREATE TABLE authors
           (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           name TEXT NOT NULL,
           name_rus TEXT,
           texts_number INTEGER NOT NULL,
           texts_percent FLOAT NOT NULL,
           """)
logging.info("Table creation finished.")

logging.info("Creating the translators table...")
db.execute("""
           CREATE TABLE translators
           (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           name TEXT NOT NULL,
           texts_number INTEGER NOT NULL,
           texts_percent FLOAT NOT NULL,
           """)
logging.info("Table creation finished.")


logging.info("Loading data from csv files to tables...")
db.execute("""LOAD DATA LOCAL INFILE 'data/corpora.csv' 
              INTO TABLE corpora 
              FIELDS TERMINATED BY ',' IGNORE 1 ROWS;""")
db.execute("""LOAD DATA LOCAL INFILE 'data/texts.csv' 
              INTO TABLE texts 
              FIELDS TERMINATED BY ',' IGNORE 1 ROWS;""")
db.execute("""LOAD DATA LOCAL INFILE 'data/authors.csv' 
              INTO TABLE authors 
              FIELDS TERMINATED BY ',' IGNORE 1 ROWS;""")
db.execute("""LOAD DATA LOCAL INFILE 'data/translators.csv' 
              INTO TABLE translators 
              FIELDS TERMINATED BY ',' IGNORE 1 ROWS;""")
db.execute("UPDATE texts SET value=NULL WHERE value='nan'")
db.execute("UPDATE texts SET value=NULL WHERE value=0")
db.execute("UPDATE texts SET value=NULL WHERE value=-1")
db.execute("UPDATE authors SET value=NULL WHERE value='nan'")
logging.info("Database creation finished.")
