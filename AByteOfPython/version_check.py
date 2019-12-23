import sys, warnings

if sys.version_info[0] > 2:
    warnings.warn('version <=3 not supported', RuntimeWarning)
else:
    print('normal code')