import os
from ttp import ttp
import json

dosyalar=[]
for file in os.listdir():
    if file.endswith('.log'):
        dosyalar.append(file)

template_proxy = """ snipped
"""

def proxy_parser(data_to_parse):
    ttp_template = template_proxy

    parser = ttp(data=data_to_parse, template=ttp_template)
    parser.parse()

    # print result in JSON format
    results = parser.result(format='json')[0]
    #print(results)

    #converting str to json. 
    result = json.loads(results)

    return(result)

parsed_proxy_parser = []

for dosya in dosyalar:
    with open(dosya) as f:
        data_to_parse = f.read()

    parsed_proxy_parser.append(proxy_parser(data_to_parse))

for i in parsed_proxy_parser:
    print(f"Name of the Node: {i[0]['Node_Name']['Node_Name']}")
    for j in i[0]['Node_Name']['Proxies']:
        if j['Oper_State'] == 'ENABLED':
            print(f"Proxy ID: {j['Proxy_ID']} --> Oper State: {j['Oper_State']}")
            
