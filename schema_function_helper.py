import pandas as pd
from json import loads, dumps

df = pd.read_csv('pokemon_tcg_cards.csv')
df_headers = list(df) #generate header

# Encode with table schema
result = df.to_json(orient="table") 
parsed = loads(result)
schema_temp = parsed['schema']['fields'] #extract values in fields key
schema_temp2 = {}
schema_temp2['BigQuery Schema'] = schema_temp # nest schema temp
schema = dumps(schema_temp2, indent=4)

# for udf
for i, j in zip(df_headers, range(0, 28)):
    print('obj.{0} = values[{1}];'.format(i, j))