#!/Users/piccolo/anaconda3/bin/python

import argparse
from ttl_analyze import TtlAnalyze
import pandas as pd
import pprint as pp
import matplotlib.pyplot as plt
from sklearn import preprocessing as prep

def tl_fix_ts(ta):
    df = ta.data
    etc = df['earthquake.time']
    TS = pd.to_datetime(etc)
    ts = [ val.date() for idx,val in TS.items() ]
    df['TS'] = ts
    ts = df['TS']
    ylist = [ val.year for idx,val in ts.items() ]
    ys = pd.Series(ylist)
    df['TS_year'] = ys
    mlist = [ val.month for idx,val in ts.items() ]
    ms = pd.Series(mlist)
    df['TS_month'] = ms

def feature_standardize(dseries, scale):
    desc = dseries.describe()
    dmean = desc['mean']
    dstd = desc['std']
    slist = (dseries - dmean)/dstd
    return slist

def tl_analyze_data(df, clist):
    #df = ta.data
    ts = df['TS']
    ys = df['TS_year']
    uyl = ys.unique()
    uys = pd.Series(uyl)
    sample_y = uys.sample(1)
    print(sample_y.values[0])
    sdf = df [ys == sample_y.values[0]] 
    cnames = sdf.columns.tolist()
    pp.pprint(cnames)
    x_val = sdf['TS'].reset_index(drop=True)
    for val in clist:
        y_val = sdf[val] #.reset_index(drop=True).values.astype(float)
        #print(y_val.describe())
        y_val_norm = feature_standardize(y_val, 5)
        plt.plot(x_val, y_val_norm)
    plt.xlabel('year')
    plt.ylabel('feature scale - standardized')
    plt.legend(clist)
    plt.show()

    return

def tl_merge_ta_and_ta2(ta, ta2):
    df1 = ta.data
    df2 = ta2.data

    df1_year = df1['TS_year']
    df2_year = df2['Year']
    df1_desc = df1_year.describe()
    df2_desc = df2_year.describe()
    f1min = df1_desc['min']
    f2min = df2_desc['min']
    f1max = df1_desc['max']
    f2max = df1_desc['max']
    ymin = 0
    ymax = 0
    if f1min > f2min:
        ymin = f1min
    else:
        ymin = f2min
    if f1max < f2max:
        ymax = f1max
    else:
        ymax = f2max
    nf1 = df1[(df1_year >= ymin) & (df1_year <= ymax)]
    nf2 = df2[(df2_year >= ymin) & (df2_year <= ymax)]
    #nf1_desc = nf1['TS_year'].describe()
    #nf2_desc = nf2['Year'].describe()
    #print(nf1['TS_year'].describe())
    #print(nf2[nf2['Year'] == 1986])
    nf1ts = nf1['TS']
    nf2yc = nf2['Year']
    co2list = []
    for idx,ts in nf1ts.items():
        nf2tmp = nf2[nf2yc == ts.year]
        nf2mnth = nf2tmp[nf2tmp['Month'] == ts.month]
        #print(nf2mnth['Carbon Dioxide (ppm)'].values)
        co2 = nf2mnth['Carbon Dioxide (ppm)']
        co2list.append(co2.values[0])
    #print(len(co2list))
    #print(nf1.shape)
    nf1['Carbon Dioxide (ppm)'] = pd.Series(co2list)
    return nf1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="File to load", type=str)

    args = parser.parse_args()

    if args.file:
        print(args.file)
    else:
        print("No file to analyze. Check usage")
        exit(0)

    file2 = "/Users/piccolo/Downloads/co2level.csv"

    clist = [ 
            'Sun.speed', 
            #'Mars.speed', 
            #'Jupiter.speed',
            'Carbon Dioxide (ppm)'
            ]

    clist2 = [
            ]

    ta = TtlAnalyze(args.file)
    if ta.data is None:
        exit(0)

    ta2 = TtlAnalyze(file2)

    print("File is loaded", ta, ta2)
    print(type(ta.data))
    tl_fix_ts(ta)
    df_merged = tl_merge_ta_and_ta2(ta, ta2)
    #co2 = df_merged[['TS', 'Carbon Dioxide (ppm)']]
    #print(co2.describe())
    tl_analyze_data(df_merged, clist)


