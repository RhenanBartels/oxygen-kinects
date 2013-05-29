#!/usr/bin/env python
# coding: utf-8

from numpy import mean
from scipy.stats import fprob


def ftest(Ernull, Eralt):
    """
    Extra-sum-square F test for two groups.
    This function allows to compare two NESTED models using the F test
    The Extra sum-of-squares F test is based on the difference between the
    sum of squares (residuals) of the two models. It also takes into account
    the number od data points and the number os parameters of each model
    (penalizes the more complicated model). It uses this information to compute
    the F ratio, from which it calculates a P value. If the simpler model (few
    parameters) is "better" P value is greater than 0.05 (5%), otherwise, if
    the more complicated model is "better" then the P value will be less than
    0.05.

    Parameters
    ----------
    Ernull : array_like
             residuals from the simpler model (null hypothesis).
    Eralt : array_like
             residuals from the more complicated model (alternative hypothesis).

    Returns
    -------
    fRatio : float
             F test from the 2 groups.
    pValue : float
             P value from F dist.


    References
    ----------

    .. [1] H.J.Motulsky  and A Christopoulos, Fitting Model to Biological Data
    using Linear and Nolinear Regression: A pratical guide to curve fitting.
    2003, GraphPad Software inc., San Diego CA, www.graphpad.com

    .. [2]  http://vassarstats.net/textbook/ch14pt1.html

    """
    sAnull = sum(Ernull)
    Nnull = len(Ernull)
    Nalt = len(Eralt)
    sAalt = sum(Eralt)
    s2Anull = sum(Ernull**2)
    s2Aalt = sum(Eralt**2)
    Mnull = mean(Ernull)  # Mean of group 1.
    Malt = mean(Eralt)  # Mean of group 2.
    SSnull = s2Anull - (sAnull**2) / Nnull
    SSalt = s2Aalt - (sAalt**2) / Nalt
    Mt = mean([Mnull, Malt])
    Nt = Nnull + Nalt
    SSwg = SSnull + SSalt  # Variability that exists inside 2 groups.
    SSbg = Nnull * (Mnull - Mt)**2 + Nalt * (Malt - Mt)**2  # measure of the
    # aggregate differences among the means of the 2 groups.
    dfbg = 1
    dfwg = (Nnull - 1) + (Nalt - 1)  # Degree of freedom of the 2 groups.
    dft = Nt - 2  # Number of degrees of freedom for the entire data.
    MSbg = SSbg / dfbg
    MSwg = SSwg / dfwg
    fRatio = MSbg / MSwg  # F Ratio.
    pValue = fprob(SSnull, SSalt, fRatio)
    return fRatio, pValue
