#!/Users/piccolo/anaconda3/bin/python

import argparse
from ttl_analyze import TtlAnalyze

def analyze_data(ta, sheets, cols):
    plot1 = {}
    plot2 = {}
    plot3 = {}
    plot4 = {}
    for idx,sName in enumerate(sheets):
        for cName in cols:
            if 0 == idx:
                plot1[cName] = sName
            elif 1 == idx:
                plot2[cName] = sName
            elif 2 == idx:
                plot3[cName] = sName
            else:
                plot4[cName] = sName
    ta.ttl_plot('Materials', plot1)
    ta.ttl_pc_plot('Materials', "Materials generated", plot2)
    ta.ttl_pc_plot('Materials', "Materials generated", plot3)
    ta.ttl_pc_plot('Materials', "Materials generated", plot4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="File to load", type=str)

    args = parser.parse_args()

    sheets = [ 
        'Materials generated',
        'Materials recycled',
        'Material combusted',
        'Materials landfilled',
    ]

    cols = [
        'Products - Metals - Aluminum',
        'Products - Plastics',
    ]

    if args.file:
        print(args.file)

    ta = TtlAnalyze(args.file)
    if ta.data is None:
        exit(0)

    print("File is loaded", ta)
    print(type(ta.data))

    analyze_data(ta, sheets, cols)

            


