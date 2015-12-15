#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     runClassification.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-15 09:28:02
# MODIFIED: 2015-12-15 09:28:03

import sys
import os
from classification import Classification

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print "sys.argv[1]: classifier"
        print "sys.argv[2]: trainFile"
        print "sys.argv[3]: devFile"
        print "sys.argv[4]: outputFile"
        exit()
        
    cfInstance = Classification(sys.argv[1], sys.argv[2], sys.argv[3])
    cfInstance.getPreResult(sys.argv[4])