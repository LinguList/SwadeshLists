# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2013-10-22 20:12
# modified : 2013-10-22 20:12
"""
Script takes all Swadesh lists from the repo and creates a csv file.
"""

__author__="Johann-Mattis List"
__date__="2013-10-22"

from glob import glob
from lingpyd import *

swads = glob('swadesh_lists/*.tsv')

D = {}
names = []
for idx,swad in enumerate(sorted(swads)):
    name = swad.split('/')[1][:-4]
    names += [name]
    data = csv2list(swad)
   
    
    # iterate over lines
    for n,g,k,i in data:

        if (k,g) not in D:
            D[k,g] = ['-' for s in range(len(swads))]
            
        D[k,g][idx] = "{0} <{1}>".format(i,n)

# set up index for regular counting of IDs
idx = 1
out = open('swadesh_list.tsv','w')
out.write('ID\tGloss\t'+'\t'.join(names)+'\n')
for key,value in sorted(D.items(),key=lambda x:x[1].count('-')):
    out.write(
            '{0}\t{1}\t'.format(idx,key[1])+'\t'.join(value)+'\n'
            )
    idx += 1
out.close()
