import pandas as pd
from database import Database

df_authors = pd.load_csv('data/authors.csv')
df_translators = pd.load_csv('data/translators.csv')

lang_names = np.array(['eng', 'arm', 'bash', 'bel', 'bul', 'bua',
                       'esp', 'ita', 'zho', 'lav', 'lit', 'ger',
                       'pol', 'ukr', 'fra', 'fin', 'cze', 'sve', 'est'])
lang_to_id = {lang_names[i]: i + 1 for i in range(len(lang_names))}
lang_to_id[np.nan] = 0

author_names = np.array(df_authors['name'])
author_to_id = {author_names[i]: i + 1 for i in range(len(author_names))}
author_to_id['nan'] = 0

def insert_text(text, lang, sphere, )