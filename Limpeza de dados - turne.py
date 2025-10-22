import pandas as pd
import numpy as np
import re
from unidecode import unidecode
from rapidfuzz import fuzz, process

# importando base de dados
df = pd.read_csv(r"Dados\turnê_dados_sujos.csv", encoding='utf-8-sig')

#identificando características da tabela
df.columns = df.columns.str.replace('\xa0', ' ', regex=True)
print(df.columns.tolist())

df["Peak"] = (df["Peak"]
                      .astype(str)
                      .str.strip()
                      .str.replace(r'[^0-9.]', '', regex=True)
                      .apply(lambda x: re.sub(r'\[.*?\]|\(.*?\)', '', x))
                      )

print(df["Peak"])