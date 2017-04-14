#!/usr/bin/env python3

""" Max Zinkus """

from sexpdata import load, car as left, cdr as right, Symbol

λ = 'λ'

class LCException(Exception):
    pass

def load_lc(filename):
    """ Load a lambda calculus file into sexpdata """
    with open(filename, 'r') as f:
        return load(f)

def parseTree(tree):
    if type(tree) == list and tree:
        if tree[0] == Symbol("+"):
            return ("((%s) + (%s))" % (
                     parseTree(tree[1]), parseTree(tree[2]))
                   ) + parseTree(tree[3:])
        elif tree[0] == Symbol("*"):
            return ("((%s) * (%s))" % (
                     parseTree(tree[1]), parseTree(tree[2]))
                   ) + parseTree(tree[3:])
        elif tree[0] == Symbol("println"):
            return ("print(%s)" % parseTree(tree[1])) + parseTree(tree[2:])
        elif tree[0] == Symbol("ifleq0"):
            return ("(%s if (%s) <= 0 else %s)" % (
                    parseTree(tree[2]), parseTree(tree[1]),
                    parseTree(tree[3]))) + parseTree(tree[4:])
        elif tree[0] == Symbol('λ'):
            return ("(lambda %s: %s)" % (parseTree(tree[1]),
                    parseTree(tree[2]))) + parseTree(tree[3:])
        elif len(tree) == 2:
            return ("(%s)(%s)" % (
                    parseTree(tree[0]),
                    parseTree(tree[1])))
        elif len(tree) == 1:
            return "%s" % parseTree(tree[0])
        elif tree:
            return "%s" % ' '.join(list(map(parseTree, tree)))
        else:
            raise LCException
    elif type(tree) == Symbol:
        return "%s" % str(tree.value())
    elif type(tree) is str:
        return tree
    elif type(tree) is int:
        return str(tree)
    return "" 

if __name__ == '__main__':
    from sys import argv
    if len(argv) > 1:
        print(parseTree(load_lc(argv[1])))
