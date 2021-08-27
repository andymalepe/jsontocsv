import json
import time
import sys
import pandas

if len(sys.argv) >= 2:
    file=sys.argv[1]
    if file.endswith('.json'):
        #Remove any new lines in json file
        data=[]
        with open(file) as f:
            for line in f:
                data.append(json.loads(line))
        #Save new dump file
        dumpFilename=file+str(time.time())
        jsonDumpFile=dumpFilename+'.json'
        with open(jsonDumpFile, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=None)
        #Read json file using Pandas into a dataframe object
        pandasDataFrame=pandas.read_json(jsonDumpFile, orient='records')
        #Output all file columns
        #print(pandasDataFrame.columns)
        #Keep specific columns
        filteredDataFrame=pandasDataFrame.filter(items=['eventid', 'timestamp', 'src_ip', 'dst_ip', 'session', 'duration', 'messagee'])
        #Convert Pfiltered dataframe to csv
        filteredDataFrame.to_csv(dumpFilename+'.csv', index=False)
    else: print('Input file is not a JSON file')
else: print('No terminal input json file')
