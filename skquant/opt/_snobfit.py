# Added this file such that the code from skquant is used istead of the package sqsnobfit


from SQCommon import Result, ObjectiveFunction
import logging, numpy
import opt.snobfit.python.SQSnobFit

log = logging.getLogger('SKQ.PyBobyqa')

log.info("""
------------------------------------------------------------------------
Coralia Cartis, et. al., "Improving the Flexibility and Robustness of
 Model-Based Derivative-Free Optimization Solvers", technical report,
 University of Oxford, (2018).
Software available at github.com/numericalalgorithmsgroup/pybobyqa/
------------------------------------------------------------------------""")

__all__ = ['minimize', 'log']


def minimize(func, x0, bounds, budget, optin, **optkwds):
    return opt.snobfit.python.SQSnobFit.minimize(func, x0, bounds, budget, optin, **optkwds) 
