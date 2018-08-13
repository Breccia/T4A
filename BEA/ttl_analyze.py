#!/Users/piccolo/anaconda3/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from ttl_logger import TtlLogger 

class TtlAnalyze(TtlLogger):
    def __init__ (self, fName):
        fSplit = fName.split('.')
        fType = fSplit[len(fSplit) - 1]
        self.fname = fName
        if 'xls' == fType or 'XLS' == fType or 'XLSX' == fType:
            try:
                xf = pd.ExcelFile(fName)
                xSheets = xf.sheet_names
                if xSheets is not None:
                    self.data = {}
                    for idx,val in enumerate(xSheets):
                        self.data[val] = xf.parse(val)
                else:
                    self.data = pd.read_excel(fName)
            except:
                tLog = "File '%s' not found" % fName
                self.ttl_log(tLog)
                self.data = None
        elif 'csv' == fType or 'CSV' == fType:
            try:
                self.data = pd.read_csv(fName)
            except:
                tLog = "File '%s' not found" % fName
                self.ttl_log(tLog)
                self.data = None
        else:
            tLog = "Unsupported file extension: " + fType
            self.ttl_log(tLog)
            raise Exception(tLog)
        return
    def ttl_get_cval(self, sName, cName):
        if sName in self.data:
            df = self.data[sName]
            cVal = df[cName]
        else:
            cVal = self.data[cName]
        return cVal
    def ttl_plot(self, cName, pData):
        hdr = []
        data = []
        width = 0.25
        mf = 0
        fig, ax = plt.subplots()
        for cVal in pData.keys():
            sName = pData[cVal]
            df = self.data[sName]
            col = df[cName]
            rVal = df[col == cVal]
            if 0 == len(hdr):
                clist = rVal.columns.tolist()
                hdr = clist[1:]
            cdata = (rVal.iloc[0]).tolist()
            tdata = cdata[1:]
            xind = np.arange(len(hdr))
            print(hdr)
            print(tdata)
            ax.bar(xind + (mf * width), tdata, width)
            ax.set_title(sName)
            mf += 1
        xind = np.arange(len(hdr))
        ax.set_ylabel('in tons')
        ax.set_xlabel('Years')
        ax.set_xticks(xind + width / 2)
        ax.set_xticklabels(hdr)
        ax.legend(pData.keys())
        plt.show()
        return
    def ttl_pc_plot(self, cName, pSheet, pData):
        hdr = []
        data = []
        width = 0.25
        mf = 0
        fig, ax = plt.subplots()
        pDF = self.data[pSheet]
        for cVal in pData.keys():
            sName = pData[cVal]
            df = self.data[sName]
            col = df[cName]
            pcol = pDF[cName]
            rVal = df[col == cVal]
            prVal = pDF[pcol == cVal]
            if 0 == len(hdr):
                clist = rVal.columns.tolist()
                hdr = clist[1:]
            cdata = (rVal[hdr]/prVal[hdr]) * 100
            tdata = (cdata.iloc[0]).tolist()
            xind = np.arange(len(hdr))
            print(hdr)
            print(tdata)
            ax.bar(xind + (mf * width), tdata, width)
            ax.set_title(sName)
            mf += 1
        xind = np.arange(len(hdr))
        ax.set_ylabel('in %')
        ax.set_xlabel('Years')
        ax.set_xticks(xind + width / 2)
        ax.set_xticklabels(hdr)
        ax.legend(pData.keys())
        plt.show()
        return

            

