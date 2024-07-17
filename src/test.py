from Neat import DAOJson

import json
import os


DATAFile = "src\\Neat\\data"
PREFIX = "Generation_"

if __name__ == "__main__":
    print(DAOJson.Read(1))

    json_dict = [{"a": 1, "b":2}]
    json_str = json.dumps(json_dict,indent=1)

    open(DATAFile+"\\"+PREFIX+str(2)+".json","w").write(json_str)

    os.remove(DATAFile+"\\"+PREFIX+str(2)+".json")