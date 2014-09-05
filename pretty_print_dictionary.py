import sys
import collections
import random
import time
import re


class Colors(object):
    def __init__(self, order='auto'):
        """
         A class represents colors for the console text.

        :type order : str
        :param order : A string that shows the way that dictionary content is displayed. possible values are<br/>

        'random': randomly choose colors for keys and values.(8 colors)
        'full': choose colors by a predefined order
        'even': choose two colors for keys and values
        """
        random.seed(time.time())
        self.order = order

        if order == 'full':
            self.colors_list = self.__get_full_foreground_color()
            self.__MAX_SIZE = len(self.colors_list)
        if order == 'even':
            self.colors_list = [35, 33]
            self.__MAX_SIZE = len(self.colors_list)

    def get_color(self, level):
        """
        Returns a color with respect of a level.

        :type level: int
        :param level: level that the dictionary exists
        """
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
        """
        Returns a string shows the end of coloring.
        """
        return '\033[0m'

    @staticmethod
    def __get_random_foreground_color():
        """
        Returns number represents the foreground color
        """
        return 30 + random.randint(1, 7)

    @staticmethod
    def __get_full_foreground_color():
        """
        Returns a list of numbers shows the color code
        """
        colors_code_list = []
        for i in xrange(1, 9):
            colors_code_list.append(30 + i)
        return colors_code_list


class PrettyDict(object):
    def __init__(self, mdict, fill_char_width=2, fill_char=' ', order='even', show_level='hide'):
        """
        A class prints a dictionary in a human readable manner
        :type mdict: dict
        :param mdict: dictionary to be displayed

        :type fill_char_width: int
        :param fill_char_width: length of indention for printing the key & value

        :type fill_char: str
        :param fill_char: string to be filled in the indention

        :type order: str
        :param order: 'full', 'even', 'random'

        :type show_level: str
        :param show_level: 'show': show the level string, 'hide': do not show a level string
        """
        self.mdict = mdict
        self.fill_char_width = fill_char_width
        self.fill_char = fill_char
        self.level = 0
        self.offset = 1
        self.__order = order
        self.show_level = show_level


    def ppd(self):
        """
        Prints the dictionary
        """
        self.__print(self.mdict, level=self.level)

    def __print(self, mdict, level=1):
        """
        Prepare the view of printing
        """
        color = Colors(self.__order)

        if not isinstance(mdict, dict):
            print >> sys.stderr, 'The given object is not a dictionary:'
        else:
            # set the current key color wrt the level of the key
            current_key_color = color.get_color(level=level)
            # for each (key, value) pair, print key and value in appropriate color
            for key in mdict.keys():
                # get the value of the corresponding key
                value = mdict[key]
                # iterate over values if value is a dictionary object
                if isinstance(value, dict):
                    # print key value in its color
                    print current_key_color + self.fill_char * (level * self.fill_char_width) + str(
                        key), (':level %d' % (level + 1)) if self.show_level == 'show' else '', color.get_end_color()
                    self.__print(value, level + 1)
                # iterate over values if value is an object of Iterable
                elif isinstance(value, collections.Iterable):
                    # get a appropriate color wrt the level of value
                    current_value_color = color.get_color(level=level + 1)
                    # print key value color
                    print current_key_color + self.fill_char * (level * self.fill_char_width) + str(
                        key), (':level %d' % (level + 1)) if self.show_level == 'show' else '', color.get_end_color()
                    # make a print statement for the values
                    r = re.compile(r'^\s+', re.MULTILINE)
                    print_statement = []
                    for v in value:
                        v = r.sub('', str(v))
                        if v != '':
                            print_statement += str(v)
                    print_statement = ','.join(print_statement)
                    # print the values in appropriate color
                    print current_value_color,
                    print self.fill_char * (level * self.fill_char_width + self.offset) + print_statement,
                    print color.get_end_color() + '\n',
                # print value if it is not iterable
                else:
                    # print the key value wrt its color
                    print current_key_color + ' ' * (level * self.fill_char_width) + str(
                        key), (':level %d' % (level + 1)) if self.show_level == 'show' else '', color.get_end_color()
                    # get appropriate color for the value wrt its level
                    current_value_color = color.get_color(level=level + 1)
                    print current_value_color,
                    print self.fill_char * (level * self.fill_char_width + self.offset) + str(mdict[key])

    def __repr__(self):
        return 'Pretty Print Dictionary'
