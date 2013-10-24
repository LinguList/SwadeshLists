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
