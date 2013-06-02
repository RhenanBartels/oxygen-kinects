#!/usr/bin/env python
# coding: utf-8

from numpy import mean, concatenate, sort, where
from scipy.stats import chisqprob


def sortIndex(v, v2):
    pos = [where(ind == v2)[0][0] for ind in v]
    return pos


def kwtest(Ernull, Eralt):
    """

    Reference
    ---------
    ..[1] http://vassarstats.net/textbook/ch14a.html

    """
    Nnull = len(Ernull)
    Nalt = len(Eralt)
    Nt = Nnull + Nalt
    rM = sort(concatenate((Ernull, Eralt), axis=1))
    rnull = sortIndex(Ernull, rM)
    ralt = sortIndex(Eralt, rM)
    sRnull = sum(rnull)
    sRalt = sum(ralt)
    aRnull = mean(rnull)
    aRalt = mean(ralt)
    aRs = (aRnull + aRalt) / 2
    SSbg = Nnull * (aRnull - aRs)**2 + Nalt * (aRalt - aRs)**2
    H = SSbg / (Nt * (Nt + 1) / 12)
    df = 1
    pValue = chisqprob(H, df)
    return H, pValue

#TODO: docstring
#TODO: copyrigth
