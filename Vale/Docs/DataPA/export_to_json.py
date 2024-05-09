import pandas as pd
import os

path = os.getcwd()
files = os.listdir(path)

list_pa_data = [f for f in files if f[-4:] == 'xlsx']


for i in range(len(list_pa_data)):
    pa_data = pd.read_excel(list_pa_data[i], sheet_name='PA_Power_Summary')
    if i == 0:
        pa_data_df = pa_data
    else:
        pa_data_df = pd.concat([pa_data_df, pa_data], ignore_index=True)

json_str = pa_data_df.to_json(orient='records')

# Using a JSON string
with open('pa_data.json', 'w') as outfile:
    outfile.write(json_str)