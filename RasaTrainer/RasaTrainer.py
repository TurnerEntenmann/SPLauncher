import sys, string, json

# <content> -> filename
def fileWrite(filename, content):
    file=open(filename, "a")
    file.write(content)
    file.close()

# <executable> -> yml formatted intent
def intStr(executable):
    intent = """
- intent: asearch
  examples: |
   - open [{0}]{{"entity": "app_name"}}
   - access [{0}]{{"entity": "app_name"}}
    """.format(executable)
    return intent

# <executable>, <synonyms> -> yml formatted synonyms
def synStr(executable,synList):
    synonym = """
- synonym: {0}
  examples: |""".format(executable)

    for syn in synList:
        synonym += """
    - """ + syn
    return synonym

# saves paths in pathFile.json
def setUp(rasaPath, rasaDataPath):
    d = {"rasaPath": path, "rasaDataPath": rasaDataPath}
    f = open("pathFile.json", "w")
    json.dump(d,f)
    f.close()

# gets rasa path from pathFile.txt
def getrasaPath():
    f = open("pathFile.txt", "r")
    path = json.load(f)["rasaPath"]
    f.close()
    return path

def getrasaDataPath():
    f = open("pathFile.txt", "r")
    path = json.load(f)["rasaDataPath"]
    f.close()
    return path

# help message
def help():
    message="""
    Usage: RasaSearcher.py <executable> <synonym 1> <synonym 2> ...
    e.g.
        RasaSearcher.py code vscode vs-code visual-studio-code
    """
    print(message)

def main():
    # usage: RasaTrainer.py <app executable> <app synonem(s)>
    # cd to rasa dir
    rasaDataPath=getrasaDataPath()
    os.chdir(rasaDataPath)
    
    # get vars
    if len(sys.argv) > 3:
        executable = sys.argv[1]
        synonyms = sys.argv[1:]

    # write to file
        intent=intStr(executable)
        fileWrite("nlu.yml",intent)
    
        syns=synStr(executable, synonyms)
        fileWrite("nlu.yml",syns)

    # train
        rasaPath=getrasaPath()
        os.chdir(rasaPath)
        os.system("rasa train")

    # set up
    if len(sys.argv) == 3:
        setUp(sys.argv[1], sys.argv[2])


    # usabilty stuff
    if sys.argv[1].lower() == "help":
        help()

    if len(sys.argv) == 1:
        message ="""
        first-time set-up:
            RasaTrainer.py <path of your rasa directory> <path of your rasa data directory>
        e.g.
            RasaTrainer.py C:\\Users\tente\source\repos\SpLauncherGit\rasaSearcher C:\\Users\tente\source\repos\SpLauncherGit\rasaSearcher\data
        
        enter 'RasaTrainer.py help' for usage"""
        


if __name__ == '__main__':
    main()

# TODO
# error handeling