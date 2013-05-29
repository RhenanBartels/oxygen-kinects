import numpy as np
from scipy.stats import fprob


def ftest(SSnull, SSalt, dfnull, dfalt):
    SSdiff = SSnull - SSalt
    dfDiff = dfnull - dfalt
    ratioF = (SSdiff /dfDiff) / (SSalt / dfalt)
    pValue = fprob(dfnull, dfalt, ratioF)
    return [ratioF, pValue]


