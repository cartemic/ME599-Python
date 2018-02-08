hw1.py

Imports:
	pandas: used to manipulate csv data because pandas is awesome
	print_function from __future__: used to make print() a function that can be used within a list comprehension

This file processes a comma-separated variable file of grades, assuming that the final grade is in the last column of the csv. Labs are assumed to contain the string "lab " (including the space, which gets rid of the possibility of finding *lab* as a substring).

IMPORTANT: Since we were not given any requirements regarding flexibility in the file name, this file also assumes that the csv is named 'grades.csv' (case sensitive). Any violation of this without an accompanying edit to the code will result in breakage. :-(

I did not directly copy-paste code (except the import I guess, for obvious reasons), but aside from python help documentation here are some links that I found helpful for addressing issues I came across:
https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value/10695175#10695175
https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
https://stackoverflow.com/questions/36685347/ignoring-non-numerical-string-values-in-pandas-dataframe
https://stackoverflow.com/questions/40144769/how-to-select-the-last-column-of-dataframe
https://stackoverflow.com/questions/20296311/printing-within-list-comprehension-in-python