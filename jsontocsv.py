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
        pandasObject=pandas.read_json(jsonDumpFile, orient='records')
        #Convert Pandas dataframe to csv
        pandasObject.to_csv(dumpFilename+'.csv', index=False)
    else: print('Input file is not a JSON file')
else: print('No terminal input json file')
