import os
OUTDIR = "output"

def printInFile(fileName:str, content:str):
    with open(os.path.join(OUTDIR, fileName), "w") as f:
        f.write(content)
        f.close()

def cleanJson(jsoncontent):
    return jsoncontent.replace("'", '"').replace("None", "null").replace("False", "false").replace("True", "true")