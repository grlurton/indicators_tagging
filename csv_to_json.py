import pandas as pd
import json

data = pd.read_csv('data/WHO_core_health_indicators.csv')

out = {}
for ID in data.ID.unique() :
    line = data.loc[data.ID == ID]
    indic = {"lib" : line.Label.to_string(index = False) ,
             "icd10" : line.ICD10.to_string(index = False) ,
             "service": {"type":line.Service.to_string(index = False)} ,
             "population" : {"age_min":line.age_min.to_string(index = False) ,
                                "age_max":line.age_max.to_string(index = False) ,
                                "gender":line.gender.to_string(index = False) } }
    out[ID] = indic

out = pd.DataFrame(out)
out = out.transpose().to_json( orient = 'records' )

with open('outputs/who_called.json', 'w') as f:
    json.dump(out, f , ensure_ascii=False)

print(out)
