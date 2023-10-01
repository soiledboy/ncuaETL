## get list of all files in /csv directory
from os import listdir
from os.path import isfile, join
import sys
sys.path.append('Users/soiledboy/dev/ncuaData/') 
import globalvariables
parent_directory = globalvariables.source_directory 

def mergeData():
    ## define tables to check against
    tables = [
    "fs220",
    "fs220A",
    "fs220B",
    "fs220C",
    "fs220D",
    "fs220E",
    "fs220G",
    "fs220H",
    "fs220I",
    "fs220J",
    "fs220K",
    "fs220L",
    "fs220M",
    "fs220N",
    "fs220P",
    "fs220Q",
    "fs220R",
    ]
    fs220 =[]
    fs220A =[]
    fs220B=[]
    fs220C=[]
    fs220D=[]
    fs220E=[]
    fs220G=[]
    fs220H=[]
    fs220I=[]
    fs220J=[]
    fs220K=[]
    fs220L=[]
    fs220M=[]
    fs220N=[]
    fs220P=[]
    fs220Q=[]
    fs220R=[]
    files = [f for f in listdir(parent_directory + "data/csv/") if isfile(join(parent_directory + "data/csv/", f))]
    ## group files into table name lists
    def check_file_name(files):
        for file_name in files:
            if file_name[-7:-4] == "220":
                fs220.append(file_name)
            elif file_name[-8:-4] == "220A":
                fs220A.append(file_name)
            elif file_name[-8:-4] == "220B":
                fs220B.append(file_name)
            elif file_name[-8:-4] == "220C":
                fs220C.append(file_name)
            elif file_name[-8:-4] == "220D":
                fs220D.append(file_name)
            elif file_name[-8:-4] == "220E":
                fs220E.append(file_name)
            elif file_name[-8:-4] == "220G":
                fs220G.append(file_name)
            elif file_name[-8:-4] == "220H":
                fs220H.append(file_name)
            elif file_name[-8:-4] == "220I":
                fs220I.append(file_name)
            elif file_name[-8:-4] == "220J":
                fs220J.append(file_name)
            elif file_name[-8:-4] == "220K":
                fs220K.append(file_name)
            elif file_name[-8:-4] == "220L":
                fs220L.append(file_name)
            elif file_name[-8:-4] == "220M":
                fs220M.append(file_name)
            elif file_name[-8:-4] == "220N":
                fs220N.append(file_name)
            elif file_name[-8:-4] == "220P":
                fs220P.append(file_name)
            elif file_name[-8:-4] == "220Q":
                fs220Q.append(file_name)
            elif file_name[-8:-4] == "220R":
                fs220R.append(file_name)

    check_file_name(files)
    import pandas as pd

    def merge_csv(file_paths, new_csv_path):
        merged_data = None
        for file_path in file_paths:
            data = pd.read_csv(file_path)
            try:
                data.rename(columns = {'CU_NUMBER':'CU_Number'}, inplace = True)
            except Exception:
                pass
            print(file_path)
            if merged_data is None:
                merged_data = data
            else:
                merged_data = pd.concat([merged_data, data], ignore_index=True)

        merged_data.to_csv(new_csv_path, index=False)

    merge_csv(fs220,"/home/tier1marketspace/ncua/merged/fs220.csv")
    merge_csv(fs220A,"/home/tier1marketspace/ncua/merged/fs220A.csv")
    merge_csv(fs220B,"/home/tier1marketspace/ncua/merged/fs220B.csv")
    merge_csv(fs220C,"/home/tier1marketspace/ncua/merged/fs220C.csv")
    merge_csv(fs220D,"/home/tier1marketspace/ncua/merged/fs220D.csv")
    merge_csv(fs220E,"/home/tier1marketspace/ncua/merged/fs220E.csv")
    merge_csv(fs220G,"/home/tier1marketspace/ncua/merged/fs220G.csv")
    merge_csv(fs220H,"/home/tier1marketspace/ncua/merged/fs220H.csv")
    merge_csv(fs220I,"/home/tier1marketspace/ncua/merged/fs220I.csv")
    merge_csv(fs220J,"/home/tier1marketspace/ncua/merged/fs220J.csv")
    merge_csv(fs220K,"/home/tier1marketspace/ncua/merged/fs220K.csv")
    merge_csv(fs220L,"/home/tier1marketspace/ncua/merged/fs220L.csv")
    merge_csv(fs220M,"/home/tier1marketspace/ncua/merged/fs220M.csv")
    merge_csv(fs220N,"/home/tier1marketspace/ncua/merged/fs220N.csv")
    merge_csv(fs220P,"/home/tier1marketspace/ncua/merged/fs220P.csv")
    merge_csv(fs220Q,"/home/tier1marketspace/ncua/merged/fs220Q.csv")
    merge_csv(fs220R,"/home/tier1marketspace/ncua/merged/fs220R.csv")




