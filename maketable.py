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
from lingpyd.meaning.basvoc import BasVoc

swads = glob('swadesh_lists/*.tsv')

mapper = dict(
        swadesh200 = 'Swadesh1952',
        swadesh100 = 'Swadesh1955',
        starostin = 'Starostin1995',
        ielex = "Wiktionary",
        ids = 'Key2007',
        asjp = 'Holman2008',
        abvd = 'Greenhill2008',
        alpher = 'Alpher1999',
        jachontov = 'Starostin1991',
        dolgo = 'Dolgopolsky1964',
        matisoff = 'Matisoff1990',
        leipzig = 'Tadmor2009',
        jach65 = 'Burlak2005',
        jach100 = 'Burlak2005',
        leijaka = 'Tadmor2009',
        swadesh100b = 'Hymes1964',

        )

D = {}
D2 = {}
names = []
idX = 1
sense = csv2list('sense_template')
senses = dict([(l[1].strip()[1:-1],l[2].strip()[1:-1]) for l in sense])

def clean(word):

    return word.split(' ')[0].lower()

for idx,swad in enumerate(sorted(swads)):
    name = swad.split('/')[1][:-4]
    names += [name]
    data = csv2list(swad)
   
    
    # iterate over lines
    for n,g,k,i in data:

        if (k,g) not in D:
            D[k,g] = ['-' for s in range(len(swads))]
            
        D[k,g][idx] = "{0} <{1}>".format(i,n)
        cg = clean(g)
        try:
            sense = senses[g]
        except KeyError:
            sense = "?"
        D2[idX] = [
                name,
                mapper[name],
                n,
                g,
                cg,
                k,
                i,
                sense
                ]
        idX += 1

# set up index for regular counting of IDs
ren = {}
idx = 1
out = open('swadesh_list.tsv','w')
out.write('ID\tOrigId\tGloss\t'+'\t'.join(names)+'\n')
for key,value in sorted(D.items(),key=lambda x:x[1].count('-')):
    out.write(
            '{0}\t{1}\t{2}\t'.format(idx,key[0],key[1])+'\t'.join(value)+'\n'
            )
    ren[key[0]] = idx
    idx += 1
out.close()

D3 = {}
for key in D2:
    D3[key] = D2[key]
    D3[key][5] = str(ren[D2[key][5]])

D3[0] = ['list','reference','number','gloss',"clean_gloss",'key','item','sense']

bv = Wordlist(D3,col='list',row='key')
bv.output('qlc',filename='swadesh_lists',formatter='list')
