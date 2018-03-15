#!/usr/bin/env python
"""
Created on Wed Mar 14 10:39:22 2018

@author: cartemic
"""

import multiprocessing as mp
import numpy as np


mp_out = mp.Queue()


def random_list(num_lists, mp_out, call_no):
    output = []
    for i in xrange(num_lists):
        output.append(list(np.random.randint(0, 10, 5)))
    mp_out.put((call_no, output))


if __name__ == '__main__':
    num_lists = 2

    processes = [mp.Process(target=random_list, args=(n, mp_out, n))
                 for n in xrange(4)]

    print 'awooga'
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print 'honka honka'
    results = [mp_out.get() for p in processes]
    print sorted(results)
