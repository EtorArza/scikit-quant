from __future__ import print_function

import logging
import subprocess
import sys
from SQCommon import Result, ObjectiveFunction


__all__ = [
    'methods',
    'minimize',
    'log',
    ]

log = logging.getLogger('SKQ')


def _check_orbit_prerequisites():
    try:
        import rpy2
        return True
    except ImportError:
        pass
    return False

def methods():
    """Returns a list of available optimizer methods"""

    m = ['imfil', 'snobfit', 'nomad', 'bobyqa']
    if _check_orbit_prerequisites():
        m.append('orbit')

    return m


def minimize(x_queue, f_queue, func, x0, bounds, budget=10000, method='imfil', options=None, **optkwds):
    optimizer = None

    method_ = method.lower()
    if 'snobfit' in method_ :
        import skquant.opt._snobfit as optimizer


    if optimizer is not None:
        return optimizer.minimize(x_queue, f_queue, func, x0, bounds, budget, options, **optkwds)

    raise RuntimeError('unknown optimizer "%s"' % method)
