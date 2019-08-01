#!/usr/bin/env python3
import crayons


def crayon():
    # print 'red string' in red
    print(crayons.red('red string'))

    # Red, White and Blue text using .format
    print(" {} white {} ".format(crayons.red('red'), crayons.blue('blue')))
crayon()

