
# coding: utf-8

# In[4]:


import csv
import sys
from datetime import date
import collections

if __name__ == '__main__':
    if len(sys.argv)<2:
        sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
        sys.exit(1)
        
    total = 0
    count = {}
    
    with open(sys.argv[1], 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['usertype']=='Subscriber':
                b_year = row['birth_year']
                count[b_year] = count.get(b_year, 0)+1
                total+=1
                
    d = collections.OrderedDict(sorted(count.items()))
    
    median_age = 0
    agg = 0
    
    for k,v in d.items():
        agg += v
        if agg*2 > total:
            median = k
            median_age = date.today().year - int(median)
            break
            
    print(median_age)

