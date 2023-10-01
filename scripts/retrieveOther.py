import requests, zipfile, io
import pandas as pd
import csv
from dateutil import parser
from azure.data.tables import TableServiceClient, EdmType, EntityProperty
from os import listdir
from os.path import isfile, join
#
period = {
    "2023-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2023-03.zip",
    "2022-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2022-12.zip",
    "2022-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2022-09.zip",
    "2022-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2022-06.zip",
    "2022-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2022-03.zip",
    "2021-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2021-12.zip",
    "2021-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2021-09.zip",
    "2021-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2021-06.zip",
    "2021-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2021-03.zip",
    "2020-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2020-12.zip",
    "2020-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2020-09.zip",
    "2020-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2020-06.zip",
    "2020-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2020-03.zip",
    "2019-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2019-12.zip",
    "2019-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2019-09.zip",
    "2019-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2019-06.zip",
    "2019-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2019-03.zip",
    "2018-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2018-12.zip",
    "2018-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2018-09.zip",
    "2018-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2018-06.zip",
    "2018-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2018-03.zip",
    "2017-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2017-12.zip",
    "2017-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2017-09.zip",
    "2017-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2017-06.zip",
    "2017-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2017-03.zip",
    "2016-12":"https://www.ncua.gov/files/publications/analysis/call-report-data-2016-12.zip",
    "2016-09":"https://www.ncua.gov/files/publications/analysis/call-report-data-2016-09.zip",
    "2016-06":"https://www.ncua.gov/files/publications/analysis/call-report-data-2016-06.zip",
    "2016-03":"https://www.ncua.gov/files/publications/analysis/call-report-data-2016-03.zip",
          }
txtFileName = []
for x in period:
    try:
        zip_file_url = period[x]
        r = requests.get(zip_file_url)
        zipdata = zipfile.ZipFile(io.BytesIO(r.content))
        zipinfos = zipdata.infolist()
        for zipinfo in zipinfos:
            zipinfo.filename = x + zipinfo.filename
            print(zipinfo.filename)
            zipdata.extract(zipinfo,path="/home/tier1marketspace/ncua/txt" , pwd=None)
            txtFileName.append(zipinfo.filename)
    except:
        pass

txtFileName[:] = [x for x in txtFileName if "Readme" not in x]
txtFileName[:] = [x for x in txtFileName if "Report1" not in x]
txtFileName[:] = [x for x in txtFileName if "TradeNames" not in x]
txtFileName[:] = [x for x in txtFileName if "AcctDesc" not in x]
txtFileName[:] = [x for x in txtFileName if "Acct-DescGrants" not in x]
txtFileName[:] = [x for x in txtFileName if "Acct-DescTradeNames" not in x]
txtFileName[:] = [x for x in txtFileName if "ATM Locations" not in x]
txtFileName[:] = [x for x in txtFileName if "Credit Union Branch Information" not in x]
txtFileName[:] = [x for x in txtFileName if "FOICUDES" not in x]
txtFileName[:] = [x for x in txtFileName if "Grants" not in x]
txtFileName[:] = [x for x in txtFileName if "ATM" not in x]
txtFileName[:] = [x for x in txtFileName if "Acct-DescCUSO" not in x]
txtFileName[:] = [x for x in txtFileName if "CUSO" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220A" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220B" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220C" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220D" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220G" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220H" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220I" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220J" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220K" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220L" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220M" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220N" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220P" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220Q" not in x]
txtFileName[:] = [x for x in txtFileName if "FS220R" not in x]


csvFileNames = [x[:-4] for x in txtFileName]
csvFileNames[:] = [x for x in csvFileNames if "Readme" not in x]
csvFileNames[:] = [x for x in csvFileNames if "Report1" not in x]
csvFileNames[:] = [x for x in csvFileNames if "TradeNames" not in x]
csvFileNames[:] = [x for x in csvFileNames if "AcctDesc" not in x]
csvFileNames[:] = [x for x in csvFileNames if "Acct-DescGrants" not in x]
csvFileNames[:] = [x for x in csvFileNames if "Acct-DescTradeNames" not in x]
csvFileNames[:] = [x for x in csvFileNames if "ATM Locations" not in x]
csvFileNames[:] = [x for x in csvFileNames if "Credit Union Branch Information" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FOICUDES" not in x]
csvFileNames[:] = [x for x in csvFileNames if "Grants" not in x]
csvFileNames[:] = [x for x in csvFileNames if "ATM" not in x]
csvFileNames[:] = [x for x in csvFileNames if "Acct-DescCUSO" not in x]
csvFileNames[:] = [x for x in csvFileNames if "CUSO" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220A" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220B" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220C" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220D" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220G" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220H" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220I" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220J" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220K" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220L" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220M" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220N" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220P" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220Q" not in x]
csvFileNames[:] = [x for x in csvFileNames if "FS220R" not in x]

y=0


for a in txtFileName:
    try:
        print(y)
        print(csvFileNames[y])
        read_file = pd.read_csv (f'/home/tier1marketspace/ncua/txt/{a}', encoding = 'cp1252')
        read_file.to_csv (f'/home/tier1marketspace/ncua/csv/{csvFileNames[y]+".csv"}', index=None )
        y=y+1
    except:
        pass

















