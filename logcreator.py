# This Software is licensed under Mozilla Public License 2.0 ( https://spdx.org/licenses/MPL-2.0.html )
import datetime

with open("log.log", "a") as logFile:
    logFile.write("\n===LOG FILE " +
                  str(datetime.datetime.now())[0:10] + " ===")


def logReturn(success, mode):
    if success is False:
        if mode == "TRUEFALSE":
            return False
        elif mode == "NUMBER":
            return 0
        elif mode == "YESNO":
            return "No"
    if success:
        if mode == "TRUEFALSE":
            return True
        elif mode == "NUMBER":
            return 1
        elif mode == "YESNO":
            return "Yes"


def log(settings):
    """Writes a line in the log file.

    Args:
        settings (dict): It's contains these:
            type (str): Can be: info; warn, warning; err, error.
            text (str): The text. E.g.: [2009-01-06 15:08:24 INFO] ->TEXT<-
            return (str): What to return? "NOTHING": Nothing | "TRUEFALSE": True or False | "NUMBER": 0 or 1 | "YESNO": Yes or No
    """
    try:
        if settings["type"].lower() not in [
            "info",
            "warn", "warning",
            "err", "error"
        ]:
            return logReturn(False, settings["return"])
        logFile = open("log.log", "a")
        time = str(datetime.datetime.now())
        #   123456789ABCDEFGHIJKLMNOPQ
        # * 2009-01-06 15:08:24.789150
        #   0123456789ABCDEFGHIJKLMNOP
        logFile.write("\n" + "[" + str(time[:19]) +
                      " " + settings["type"].upper() + "] " + settings["text"])
    except:
        return logReturn(False, settings["return"])
    else:
        return logReturn(True, settings["return"])
    finally:
        logFile.close()


if __name__ == '__main__':
    print(log({
        "type": "INFO",
        "text": "Never gonna give you up!",
        "return": "TRUEFALSE"
    }))
    print(log({
        "type": "WARN",
        "text": "Never gonna let you down!",
        "return": "NUMBER"
    }))
    print(log({
        "type": "ERROR",
        "text": "Never gonna run around and desert you!",
        "return": "YESNO"
    }))
    print(" \nCovered Software is provided under this License on an \"as is\" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the Covered Software is free of defects, merchantable, fit for a particular purpose or non-infringing. The entire risk as to the quality and performance of the Covered Software is with You. Should any Covered Software prove defective in any respect, You (not any Contributor) assume the cost of any necessary servicing, repair, or correction. This disclaimer of warranty constitutes an essential part of this License. No use of any Covered Software is authorized under this License except under this disclaimer. \n")
    print("\nSorry, but the logcreator is not a (G)UI project!")
    while True:
        notImportant = datetime.datetime.now()
