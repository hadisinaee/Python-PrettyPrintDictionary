from pretty_print_dictionary import PrettyDict

d = {'a': 0, '1': {1: 'c', 2: 'd'}}
pd = PrettyDict(d, fill_char='*', fill_char_width=4, show_level='hide')
pd.ppd()


