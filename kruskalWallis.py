#!/usr/bin/env python
# coding: utf-8

from numpy import mean, concatenate, sort, where
from scipy.stats import chisqprob


def sortIndex(v, v2):
    pos = []
    for itr in xrange(len(v)):
        ind = where(v[itr] == v2)[0][0]
        pos.append(ind)
    return pos


def kwtest(Ernull, Eralt):
    Nnull = len(Ernull)
    Nalt = len(Eralt)
    Nt = Nnull + Nalt
    rM = sort(concatenate((Ernull, Eralt), axis=1))
    rnull = sortIndex(Ernull, rM)
    ralt = sortIndex(Eralt, rM)
    sRnull = sum(rnull)
    sRalt = sum(ralt)
    sRc = sRnull + sRalt
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
