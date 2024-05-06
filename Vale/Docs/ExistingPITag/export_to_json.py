import pandas as pd

pi_tag_list = pd.read_excel('PI_Tag_Resume.xlsx', sheet_name="pi_tag_list")
json_str = pi_tag_list.to_json(orient='records')

# Using a JSON string
with open('json_data.json', 'w') as outfile:
    outfile.write(json_str)
