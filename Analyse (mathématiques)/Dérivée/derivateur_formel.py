# -*- coding: utf-8 -*-

import os
from math import exp, log, cos, sin


class expr:

    def __init__(self, valeur, gauche, droite):
        self.val = valeur
        self.g = gauche
        self.d = droite

    def __add__(self, other):
        if self.val == 0:
            return other
        if other.val == 0:
            return self
        if type(self.val) != str and type(other.val) != str:
            return expr(self.val + other.val, None, None)
        if type(other.val) != str and other.val < 0:
            return expr('-', self, -other)
        return expr('+', self, other)

    def __pow__(self, k):
        if k.val == 1:
            return self
        if k.val == 0:
            return expr(1, None, None)
        return expr('**', self, k)

    def __truediv__(self, other):
        if other.val == 1:
            return self
        return self * (other ** expr(-1, None, None))

    def __mul__(self, other):
        if self.val == 0 or other.val == 0:
            return expr(0, None, None)
        if self.val == 1:
            return other
        if other.val == 1:
            return self
        if type(self.val) != str and type(other.val) != str:
            return expr(self.val * other.val, None, None)
        return expr('*', self, other)

    def __neg__(self):
        if self.val in {'*', '+', '**', 'cos', 'sin', 'ln', 'exp'}:
            return expr(-1, None, None) * self
        return expr(-self.val, None, None)

    def __sub__(self, other):
        return expr('-', self, other)

    def __repr__(self):
        def par(v):
            if v.g == None:
                return str(v)
            return '(' + str(v) + ')'
        if self.val in {'+', '-', '*', '/'}:
            return par(self.g) + self.val + par(self.d)
        if self.val in {'ln', 'cos', 'sin', 'exp'}:
            return self.val + '(' + str(self.g) + ')'
        if self.val == '**':
            if self.d.val == 1:
                return str(self.d)
            if self.d.val == 0.5:
                return 'R(' + str(self.g) + ')'
            if type(self.d.val) == str or self.d.val > 0:
                return par(self.g) + '^' + par(self.d)
            else:
                return '1/' + par(self.g ** (-self.d))
        return str(self.val)

    def eval(self, var, nb):
        if self.val == '+':
            return (self.g.eval(var, nb)) + (self.d.eval(var, nb))
        if self.val == '-':
            return (self.g.eval(var, nb)) - (self.d.eval(var, nb))
        if self.val == '*':
            return (self.g.eval(var, nb)) * (self.d.eval(var, nb))
        if self.val == '/':
            return (self.g.eval(var, nb)) / (self.d.eval(var, nb))
        if self.val == '**':
            return (self.g.eval(var, nb)) ** (self.d.eval(var, nb))
        if self.val == 'ln':
            return log(self.g.eval(var, nb))
        if self.val == 'cos':
            return cos(self.g.eval(var, nb))
        if self.val == 'sin':
            return sin(self.g.eval(var, nb))
        if self.val == 'exp':
            return exp(self.g.eval(var, nb))
        if self.val == var:
            return nb
        if type(self.val) == str:
            raise ValueError('Évaluation avec un paramètre impossible')
        return self.val

    def deriv(self, var):
        if self.val == var:
            return expr(1, None, None)
        if self.val == '+':
            return self.g.deriv(var) + self.d.deriv(var)
        if self.val == '-':
            return self.g.deriv(var) - self.d.deriv(var)
        if self.val == '*':
            return (self.g.deriv(var) * self.d) + (self.d.deriv(var) * self.g)
        if self.val == '/':
            return ((self.g.deriv(var) * self.d) - (self.d.deriv(var) * self.g)
                    / (self.d ** expr(2, None, None)))
        if self.val == '**':
            return self.d * self.g.deriv(var) * (self.g ** (self.d - expr(1, None, None)))
        if self.val == 'ln':
            return self.g.deriv(var) / self.g
        if self.val == 'exp':
            return self.g.deriv(var) * self.g
        if self.val == 'cos':
            return -self.g.deriv(var) * expr('sin', self.g, None)
        if self.val == 'sin':
            return self.g.deriv(var) * expr('cos', self.g, None)
        return expr(0, None, None)

    def derivn(self, n, var):
        if n == 0:
            return self
        return (self.deriv(var)).derivn(n - 1, var)

# Des racourcis :


def Ln(e):
    return expr('ln', e, None)


def Cos(e):
    return expr('cos', e, None)


def Sin(e):
    return expr('sin', e, None)


def Exp(e):
    return expr('exp', e, None)


def Const(k):
    return expr(k, None, None)


def Var(x):
    return expr(x, None, None)

f = Ln(Ln(Ln(Var('x'))))
print(f.deriv('x'))

g = (Var('x') + Const(1)) ** Var('k')
print(g)
g.deriv('x')

f = Cos(Var('x'))
f5 = f.derivn(5, 'x')
print(f5.eval('x', 0))

os.system("pause")
