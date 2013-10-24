SwadeshLists
============

This is simple table data that maps different Swadesh lists onto common concepts. At the moment, I'm not sure where it will lead in the end, but we start with simple concept-string mappings for all items in different Swadesh lists that may later be expanded by additional rankings and the like.

Currently, all data contained in the folder of separate Swadesh lists is provided in a simple tab-delimited text format: [swadesh_lists.tsv](https://github.com/LinguList/SwadeshLists/blob/master/swadesh_list.tsv). A more verbose fileformat for the data is also accessible as [swadesh_lists.qlc](https://github.com/LinguList/SwadeshLists/blob/master/swadesh_lists.qlc). This format can be used for parsing it in [LingPy](https://github.com/lingpy/lingpy). The simple table format lists a basic gloss and a unique ID in the first two columns, and the items for all lists currently combined in the following columns. Numbers that are provided with the original lists are added in greate/less-brackets after the entry.

The references for all files are not yet complete and will be added in the future.

## How concepts are mapped among different Swadesh Lists

As a basis, we shall use the WOLD meanings (http://wold.livingsources.org/). All concepts in the WOLD are preanalyzed in an initial step and split into separate concepts, if the original WOLD concept contains multiple concepts strings, we split it into separate concepts. For example, the entry:

* the rock or stone

will be rendered as

* the rock
* the stone

while at the same time a reference to the original WOLD source will be kept.

In order to ease the search for concepts, we allow for "synonym aliases". Aliases are a set of concept strings that help us identify the basic concepts when adding new lists to the database.
For example, the WOLD concept "the soil" will usually be rendered as "earth" or "earth (soil)" in typical Swadesh lists.
Using an alias "the earth" that links directly to "the soil" helps us to identify the correct concepts here. This is more a practical than a theoretical enterprise, yet it can be extremely helpful in quickly mapping new Swadesh lists to our growing database.

### Rules for mapping

Mapping is complicated. For example, given the concept string "hot" in one Swadesh list, and the concept string "warm (hot)" in another one, are we correct in mapping the two concepts? Even more complicated are "burn (transitive)" and "burn (intransitive)", or simpley "burn". The strategy we use here to overcome this problem is as follows:

* only the main concepts are linked to our basic, what is in brackets won't be linked (thus, "fat (grease)" will ONLY be linked to "THE FAT", not to "THE GREASE",
* if multiple concepts are given separated by a comma or a slash, all concepts will be mapped separately,
* additionally, mergers of near synonyms will be defined that help us to map those concept that are often merged in Swadesh lists, as a result, a merger is defined between "THE FAT" and "THE GREASE", and if needed, both concepts can be displayed in a "merged fashion" when comparing different Swadesh lists.

Note that this procedure may lead to certain problems in specific cases. For example, the entry "man/male" in the ABVD Swadesh list is not very clear: is the "male" meant to refer to the adjective "male" or the noun "the male"? Without a background in Austronesian linguistics, this question cannot be solved from the source alone: it may be possible, that we are dealing with a common semantic merger between "male (adjevtive)" and "the man" here (as we find it often between "sun" and "day" in South-East-Asian languages, for example), but the other explanation seems also possible. The splitting of Swadesh entries into separate concepts in our base list is inevitable, but it may also be erroneous. However, errors may be corrected in the future, and if one reading turns out to be obviously wrong, we can change it afterwards.

However, the rule of thumb to split Swadesh entries that contain a comma or a slash, and to ignore what's in the brackets (by ignore, I mean, that it won't be mapped separatedly to the concept list) seem inevitable in order to guarantee a maximally transparent working process in the initial stages.

### Aliases

All basic concepts in the "concepticon" can be extended by "aliases". This is a simple list of further glosses that can be used to ease the search for concept mappings. This is mainly for practical reasons and does not reflect any theoretic principles. In practice, however, it turns out to be very useful.

### Near Synonym Mergers

With the data, a list (constantly growing) of near semantic mergeres will be provided. In this list, we store all cases that are obviously merged in the literature, or in the languages of the world. The list is a simple comma-separated file containing all concept strings. Currently, it contains, among others, the row

```text
to burn (transitive), to burn (intransitive)
```
since these two concepts are often left undistinguished in Swadesh lists. ABVD, for example, makes no distinction between the two, Swadesh 100 (1955) lists only "burn transitive", but Swadesh 200 (1952) lists "burn intransitive". However, commonly, the "shared items" between Swadesh 100 and Swadesh 200 also list "burn". This shows, that scholars make some implicit assumption that these two concepts can be merged under many circumstances. The list of "near semantic mergers" will help us to keep the lists comparable, although regarding certain entries they are not from a strict perspective.

## Roadmap

Current ideas include the following working procedure:

* write a basic scripts that eases the mapping of Swadesh lists with our basic concepts (partially already finished)
* map more and more Swadesh lists to our growing database of basic concepts (four lists already added, many lists are already available in digital form)
* add new concepts to the basic list, where necessary
* add new "near semantic mergers", where they become apparent
* write a basic datatype for LingPy that reads in the mappings and deals with them in such a way that
  - subsets of two lists can be extracted (taking one as the source of the other)
  - lists can be merged into larger lists
  - known scalings or rankings can be transferred from one list to the concepts of the other
  - lists can be created automatically in different languages


Certain steps of this roadmap are already taken, but there's still much more to do in the future. 
