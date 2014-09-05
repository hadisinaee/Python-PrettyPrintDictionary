from pretty_print_dictionary import PrettyDict


dict_1 = {'a': 0, '1': {1: {'abc': [1, 2, 3, 4, 5, 6], 'efg': [7, 8, 9, 10, 100]},
                        2: {'1': {1: 'abc', 2: 'efg'}, '2': {3: 'abc'}}}, '2': [1, 2, 3, 4, 5, 6]}
print dict_1

pd = PrettyDict(dict_1, fill_char=' ', fill_char_width=4, show_level='show', order='even')
pd.ppd()
