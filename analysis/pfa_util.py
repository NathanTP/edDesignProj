import pandas as pd
import numpy as np
import math
from collections import namedtuple

x86Freq = 2594220226
rvFreq = 3200000000

RunRes = namedtuple('RunRes', ['mean', 'std'])

# Read a run file and returns a dictionary of cleaned and normalized dataframes
# for each benchmark, indexed by size.
#
# runPath = path to file containing performance results for this run
# runFreq = frequency to use for cycles in this run (cycles/sec)
def ingest_run(runPath, platform):
    if platform == 'rv':
        runFreq = rvFreq
    elif platform == 'x86':
        runFreq = x86Freq
    else:
        print("Unrecognized platform: " + platform)

    res = pd.read_csv(runPath, header=0, comment='#')

    # Times from cycles to seconds
    res['t_run'] = res['t_run'] / runFreq
    res['t_bookkeeping'] = res['t_bookkeeping'] / runFreq
    res['t_rmem_write'] = res['t_rmem_write'] / runFreq
    res['t_rmem_read'] = res['t_rmem_read'] / runFreq
    res['t_fault'] = res['t_fault'] / runFreq
    res['t_kpfad'] = res['t_kpfad'] / runFreq

    benchs = {}
    for Bname in res.benchmark.unique():
        # XXX ignore qsort benchmark for now
        if Bname == 'qsort' or Bname == 'pagerank':
            continue

        Bres = res.loc[res['benchmark'] == Bname].copy()
        # Drop columns that we aren't using
        Bres.drop(['benchmark', 'datetime', 'run', 'command'], inplace=True, axis=1)

        # Size from absolute to "%local"
        workingSz = max(Bres['size'])
        Bres['size'] = (Bres['size'] / workingSz)*100

        # Calculate mean/std
        means = Bres.groupby(['size']).mean()
        stds = Bres.groupby(['size']).std()
        Bres = RunRes(means, stds)
        
        # Add 'Slowdown' column
        maxTime = Bres.mean.loc[100, 't_run']
        Bres.mean['slowdown'] = Bres.mean['t_run'] / maxTime
        Bres.std['slowdown'] = Bres.std['t_run'] / maxTime

        # Delete columns/rows that aren't needed for later analysis (cleans up printouts)
        # Bres.mean.drop(100, inplace=True, axis='index')
        # Bres.std.drop(100, inplace=True, axis='index')
        # Bres.mean.drop(['t_run'], inplace=True, axis=1)
        # Bres.std.drop(['t_run'], inplace=True, axis=1)
        
        # Figures look better when we go from 75%-25%
        Bres.mean.sort_index(axis='index', inplace=True, ascending=False)
        Bres.std.sort_index(axis='index', inplace=True, ascending=False)
       
        benchs[Bname] = Bres

    return benchs 

def ingest_pflat(Path):
    res = pd.read_csv(Path, header=0, comment='#')

    platforms = {}
    for Pname in res.platform.unique():
        Pres = res.loc[res['platform'] == Pname].drop(['platform'], axis=1).copy()
        if Pname == 'x86':
            Pres = Pres / x86Freq
        else:
            Pres = Pres / rvFreq

        Pmean = Pres.mean().rename('mean')
        Pstd = Pres.std().rename('std')
        Pmin = Pres.min().rename('min')
        Pmax = Pres.max().rename('max')
        platforms[Pname] = pd.concat([Pmean, Pstd, Pmin, Pmax], axis=1)

    return platforms

def ingest_micro(Path):
    res = pd.read_csv(Path, header=0, comment='#')

    # Convert to ns
    res['x86RamSwap'] = res['x86RamSwap'] / x86Freq
    res['PFA'] = res['PFA'] / rvFreq
    res['rvSW'] = res['rvSW'] / rvFreq
    res['rvRamSwap'] = res['rvRamSwap'] / rvFreq

    return RunRes(
            res.groupby('measurement').mean(),
            res.groupby('measurement').std())

# print(ingest_pflat('raw/pflat.csv'))
# x86freq = 2594220226
# print(ingest_run('raw/results_x86.csv', 'x86'))
# ingest_run('raw/results_x86.csv', 'x86')
