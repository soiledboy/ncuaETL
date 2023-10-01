
from os import listdir
from os.path import isfile, join
## define tables to check against
def mergeOtherData():
    tables = [
    "FOICU",
    ]
    FOICU =[]

    ## get list of all files in /csv directory
    files = [f for f in listdir("/home/tier1marketspace/ncua/csv/") if isfile(join("/home/tier1marketspace/ncua/csv/", f))]
    ## group files into table name lists
    def check_file_name(files):
        for file_name in files:
            if file_name[-9:-4] == "FOICU":
                FOICU.append(file_name)

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

    merge_csv(FOICU,"/home/tier1marketspace/ncua/merged/FOICU.csv")





