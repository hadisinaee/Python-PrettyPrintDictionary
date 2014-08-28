import sys
import collections
import random
import time


class Colors:
    def __init__(self, order='auto'):
        random.seed(time.time())
        self.__fg_colors = []
        self.__bg_colors = []
        self.order = order

        if order == 'full':
            self.colors_list = self.__get_full_foreground_color()
            self.__MAX_SIZE = len(self.colors_list)
        if order == 'even':
            self.colors_list = [35, 33]
            self.__MAX_SIZE = len(self.colors_list)

    def get_color(self, level):
        if self.order == 'even':
            return '\033[' + str(self.colors_list[(level - 1) % self.__MAX_SIZE]) + 'm'
        if self.order == 'full':
            return '\033[' + str(self.colors_list[(level - 1) % self.__MAX_SIZE]) + 'm'
        if self.order == 'random':
            return '\033[' + str(self.__get_random_foreground_color()) + 'm'
        else:
            return '\033[' + str(self.__get_random_foreground_color()) + 'm'

    @staticmethod
    def get_end_color():
        return '\033[0m'

    @staticmethod
    def __get_random_foreground_color():
        return 30 + random.randint(1, 7)

    @staticmethod
    def __get_full_foreground_color():
        colors_code_list = []
        for i in xrange(1, 9):
            colors_code_list.append(30 + i)
        return colors_code_list


class A(object):
    def __repr__(self):
        return "A"


class B(object):
    def __repr__(self):
        return "B"


class PrettyDict(object):
    def __init__(self, mdict, fill_char_width=2, fill_char=' ', order='even'):
        self.mdict = mdict
        self.temp_mdict = mdict
        self.fill_char_width = fill_char_width
        self.fill_char = fill_char
        self.level = 0
        self.offset = 1
        self.__order = order


    def ppd(self):
        self.__print(self.mdict, level=self.level)

    def __print(self, mdict, level=1):
        color = Colors(self.__order)
        if not isinstance(mdict, dict):
            print >> sys.stderr, 'The given object is not a dictionary:'
        else:
            current_key_color = color.get_color(level=level)
            for key in mdict.keys():
                value = mdict[key]
                if isinstance(value, dict):
                    print current_key_color + ' ' * (level * self.fill_char_width) + str(
                        key), ':level %d' % (level + 1), color.get_end_color()
                    self.__print(value, level + 1)
                elif isinstance(value, collections.Iterable):
                    current_value_color = color.get_color(level=level + 1)
                    print_statement = []
                    print current_key_color + ' ' * (level * self.fill_char_width) + str(
                        key), ':level %d' % (level + 1), color.get_end_color()
                    for v in value:
                        print_statement += str(v)
                    print_statement = ','.join(print_statement)
                    print current_value_color,
                    # print print_statement.rjust(level * self.fill_char_width + self.offset + len(print_statement),
                    #                             self.fill_char),
                    print ' ' * (level * self.fill_char_width + self.offset) + print_statement,
                    print color.get_end_color() + '\n',

    def __repr__(self):
        return 'Pretty Print Dictionary'


ppd = PrettyDict({A(): {1: [1, 2, 3]}, B(): {2: {3: [1, 2, 3, 5, 4, 3, 2]}, 4: ['a', 'b']}, 3: ['a', 'b']},
                 order='full')

# ppd = PrettyDict({B(): {2: {3: [1, 2, 3, 5, 4, 3, 2]}}})
# print str(ppd)
ppd.ppd()
# c = Colors()
# print c.get_color(), 'hadi'