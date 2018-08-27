#!/Users/piccolo/anaconda3/bin/python

import time

class TtlLogger:
    def __init__ (self):
        return
    def ttl_log(self, lStr):
        tStr = time.asctime()
        tLog = tStr + ' - ' + lStr
        print(tLog)
        return
