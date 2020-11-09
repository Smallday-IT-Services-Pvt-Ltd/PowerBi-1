import csv
import pandas as pd

class PowerBI:
    def __init__(self):
        pass

    def get_data(self,fpath):
        df_names = []
        nof = -1
        with open(fpath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            line_count = 0
            for row in csv_reader:
                line_count = line_count + 1
                if row[0].startswith("!"):
                    nof = nof + 1
                    df_names.append(row[0][1:])
                    dic = {}
                    for x in row:
                        dic[x] = []
                    continue
                co = 0
                for i in dic.keys():
                    dic[i].append(row[co])
                    co = co + 1
                if not (row[0].startswith("!")):
                    df = pd.DataFrame(dic)
                    df.to_csv(df_names[nof] + '.csv')










