import sys
sys.path.append("../ncuadata/scripts")
sys.path.append("../ncuadata/scripts")
import mergeData
import mergeOtherData
import retrieveData
import uploadData
import makeHeadersData
import upload2Data

retrieveData()
mergeData()
mergeOtherData()
uploadData()
makeHeadersData()
upload2Data()