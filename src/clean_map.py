import pandas as pd 
from pathlib import Path
from wdcuration import lookup_multiple_ids

HERE = Path(__file__).parent.resolve()
DATA = HERE.parent.joinpath('data').resolve()
RESULTS = HERE.parent.joinpath('results').resolve()

df = pd.read_excel(DATA/"icd-10-to-meddra-map---june-2023---codes-mapping.xlsx", dtype=str,skiprows=1)

equivalent_df = df[df["Map Attribute"] == "Equivalent"]

equivalent_df.to_csv(DATA/ "equivalent_map.csv", index=False)

icd_codes = equivalent_df['ICD-10 Code'].unique().astype(str)



# Lookup the Wikidata QIDs for drugs and events
icd_based_qids = lookup_multiple_ids(list_of_ids=icd_codes, wikidata_property='P494')

equivalent_df["Wikidata ID"] = equivalent_df["ICD-10 Code"].map(icd_based_qids)

equivalent_df.to_csv(DATA/ "equivalent_map.csv", index=False)
