from pretty_print_dictionary import PrettyDict

dict_1 = {'a': 0, '1': {1: 'c', 2: 'd'}}
print dict_1
pd = PrettyDict(dict_1, fill_char=' ', fill_char_width=2, show_level='hide')
pd.ppd()


class A(object):
    def __repr__(self):
        return 'A'


a = A()
dict_2 = {a: '1 \t     2 \t \t \t \n\n 3', 1: [1, 2, 3, 4]}
pd = PrettyDict(dict_2, fill_char=' ', fill_char_width=3, show_level='show')
pd.ppd()



