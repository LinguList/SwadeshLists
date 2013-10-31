# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2013-10-23 19:29
# modified : 2013-10-23 19:29
"""
Add new swadesh list to all existing lists.
"""

__author__="Johann-Mattis List"
__date__="2013-10-23"

from lingpyd import *
from sys import argv
from re import *

meta = csv2list('meta/meta.tsv')

# get maximal id of meta
maxIdx = max([int(l[0]) for l in meta])+1
oldIdx = maxIdx

# cleaning function
def clean(word):
    word = word.strip()

    if word.startswith('to '):
        word = word[word.index(' '):]
    if word.startswith('the '):
        word = word[word.index(' '):]
    if '(' in word:
        word = word[:word.index('(')]
    if word.endswith('?'):
        word = word[:word.index('?')]

    return word.strip()

# make a fuzzy matcher
fuzzy = {}

for line in meta:
    
    if line[1] != "IGNORE":
        try:
            fuzzy[line[3]] += [line[2]]
        except KeyError:
            fuzzy[line[3]] = [line[2]]
        
        if line[-1] != '-':
            for a in line[-1].split(','):
                try:
                    fuzzy[a] += [line[2]]
                except:
                    fuzzy[a] = [line[2]]

metaIdx = dict([(l[2],l[0]) for l in meta])


# make filename for easy reference
fname = 'swadlists_original/'+argv[1]

# load the swadesh list
sw = csv2list(fname+'.tsv')
swnew = []


# check for loaded file
try:
    out = csv2list(fname.replace('original','edited')+'.tsv')
    last_line = out[-1][2:]
    for i,line in enumerate(sw):
        if line == last_line:
            break
    idx = i
    for line in out:
        swnew += [line]
    out = open(fname.replace('original','edited')+'.tsv','w')
    for line in swnew:
        out.write(
                '\t'.join(
                    ["{0}".format(x) for x in line]
                    )+'\n'
                )
    out.close()

except:
    idx = 1
    swnew += [["Key","Concept"]+sw[0]]
    out = open(fname.replace('original','edited')+'.tsv','w')
    out.write('\t'.join(swnew[-1])+'\n')
    out.close()
dups = 0
for line in sw[idx:]:
    swnew = []
    n,g = line[0],line[1]
    
    # check for direct match
    if g.upper() in metaIdx:
        g = g.upper()
        print("[i] Found direct match for «{0}».".format(g))
        swnew += [[metaIdx[g],g]+line]

    #for g in gg:
    else:
        # check whether it's there
        if g in fuzzy:
            if len(fuzzy[g]) == 1:
                print("[{1}] Direct match found for «{0}».".format(g,n))
                swnew += [[metaIdx[fuzzy[g][0]],fuzzy[g][0]]+line]
            else:
                print("[{1}] Multiple matches found for «{0}».".format(g,n))
                print("... "+', '.join(fuzzy[g]))
                answers = input("[?] Which one should be inserted? ")
                if answers.isdigit():
                    swnew += [
                            [
                                metaIdx[fuzzy[g][int(answers)-1]],
                                fuzzy[g][int(answers)-1]]+line
                            ]
                elif ',' in answers and sum([1 for a in answers.split(',') if a.isdigit()]) == len(answers.split(',')):
                    for a in answers.split(','):
                        swnew += [
                                [
                                    metaIdx[fuzzy[g][int(a)-1]],
                                    fuzzy[g][int(a)-1]]+line
                                ]
                else:
                    for a in answers.split(','):
                        swnew += [[metaIdx[a],a]+line]

                #for answer in answers.split(','):
                #    swnew += [[metaIdx[answer],answer]+line]
        else:
            answers = input("[{1}] Entry «{0}» could not be found in database, do you have an idea? ".format(g,n))
            if answers == 'x':
                answers = g.replace('/',',')
            elif answers == 's':
                answers = ','.join([clean(x) for x in g.split(',')])

            for answer in answers.split(','):
                answer = answer.strip()
                if answer in fuzzy:
                    if len(fuzzy[answer]) == 1:
                        print("[i] Found match for entry «{0}».".format(answer))
                        swnew += [[metaIdx[fuzzy[answer][0]],fuzzy[answer][0]]+line]
                    else:
                        print("[{1}] Entry «{0}» has multiple counterparts in the metalist.".format(answer,n))
                        print("[:] "+','.join(fuzzy[answer]))
                        answer2 = input("[?] Which one do you mean? " )
                        if answer2.isdigit():
                            swnew += [
                                    [
                                        metaIdx[fuzzy[answer][int(answer2)-1]],
                                        fuzzy[answer][int(answer2)-1]]+line
                                    ]
                        else:
                            for a in answer2.split(','):
                                print(a)
                                swnew += [[metaIdx[a],a]+line]
                else:
                    print("[{1}] Entry «{0}» could not be found in database.".format(answer,n))
                    answer = input("[?] How should it be rendered in the database? " )
                    if answer not in "n":
                        meta += [[maxIdx,0,answer]+ 8 * ["-"]]
                        fuzzy[clean(answer)] = [answer]
                        metaIdx[answer] = maxIdx
                        maxIdx += 1
                        swnew += [["?","?"]+line]
                    else:
                        swnew += [["?","?"]+line]
    out = open(fname.replace('original','edited')+'.tsv','a')
    for line in swnew:
        out.write(
                '\t'.join(
                    ["{0}".format(x) for x in line]
                    )+'\n'
                )
    out.close()
    if maxIdx > oldIdx:
        out = open('meta/_meta_new.tsv','w')
        for line in meta:
            out.write(
                    '\t'.join(
                        ["{0}".format(x) for x in line]
                        )+'\n'
                    )
        out.close()
        oldIdx = maxIdx
    if len(swnew) > 1:
        dups += len(swnew) - 1

print("[i] Finished processing the Swadesh list, inserted {0} entries, and {1} duplicates.".format(len(sw)-1,dups))

