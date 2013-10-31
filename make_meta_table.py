# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2013-10-31 09:31
# modified : 2013-10-31 09:31
"""
Make a large meta-table of processed Swadesh lists.
"""

__author__="Johann-Mattis List"
__date__="2013-10-31"

from swd_lib.csv import csv2list
from glob import glob

# load meta-file
meta = csv2list('meta/meta.tsv')

# glob the swadesh lists
swds = glob('swadlists_edited/*.tsv')

D = {}

# iterate over lists
for swd in sorted(swds):

    # get index
    idx = sorted(swds).index(swd)

    lst = csv2list(swd)[1:]
    
    for k,c,n,g in lst:
        
        # check for presence of key
        if (k,c) not in D:
            D[(k,c)] = ['' for x in swds]

        D[k,c][idx] = '»{0}« #{1}'.format(g,n)

f = open('swadlists.tsv','w')
f.write('Key\tConcept\t'+'\t'.join([x.replace('swadlists_edited/','') for x in sorted(swds)])+'\n')
for k,c in sorted(D,key=lambda x:sum([1 for a in D[x] if a]),reverse=True):
    f.write('\t'.join([k,c]+D[k,c])+'\n')
f.close()
