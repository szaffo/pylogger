import datetime

LOG_FILE = "log.txt"
# LOG_FILE = "put/four/filepath.here"


def log(text, error=None):

    text = "{} {: <5} {}".format(
        datetime.datetime.now().strftime('[%Y.%m.%d %H:%M:%S]'),
        text.split(" ")[0],
        " ".join(text.split(" ")[1:])
    )

    if error != None:
        text += " [ERROR] " + str(error)

    with open(LOG_FILE, 'a') as f:
        f.write(text  + "\n")


def getLog():
    with open(LOG_FILE, 'r') as f:
        data = f.read().strip().split("\n")

    return data


def printLog():
    print(getLog())


def clearLog():
    with open(LOG_FILE, 'w') as f:
        f.write("")

def getLogSize():
    return len(getLog())


if __name__ == '__main__':
    try:
        raise Error("Test")
    except Exception as e:
        log("TEST alma", error=e)

    log("TEST kalapács")

    printLog()
    print(getLogSize())
    clearLog()
