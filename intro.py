import requests

import re
import pandas as pd

with open ('processor_table.csv', 'w') as f:
    f.write('PROCESSOR, CORES')
    f.write('\n')
    for i in range(1, 12):
        res = requests.get(f'https://www.intel.co.uk/content/www/uk/en/products/processors/xeon/view-all.html?page={i}')
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        for div in soup.find_all('div', {'class': 'content-wrap valign-btm'}):
            processor = re.search(r'\w{0,1}\-?\d{4}\w{0,2}\s?[v]?\d?', div.span.string.strip().replace(' ', '')).group()
            for li in div.find_all('li'):
                if 'Cores' in li.string:
                    cores = li.string
            f.write(f'{processor}, {cores}')
            f.write('\n')
            
            
    
            







