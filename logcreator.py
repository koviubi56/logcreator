# This Software is licensed under Mozilla Public License 2.0 ( https://spdx.org/licenses/MPL-2.0.html )
import datetime

logFile = open("log.log", "a")
logFile.write("\n===LOG FILE " +
              str(datetime.datetime.now())[0:10] + " ===")
logFile.close()


def log(type, text, return):
    """Writes a line in the log file.

    Args:
        type (str): Can be: i, inf, info; w, warn, warning; e, err, error.
        text (str): The text. E.g.: [2009-01-06 15:08:24 INFO] ->TEXT<-
        return (str): What to return? "NOTHING": Nothing | "TRUEFALSE": True or False | "NUMBER": 0 or 1 | "YESNO": Yes or No

    Returns:
        str: [WRITE]
    """
    try:
        if type.lower() not in [
            "i", "inf", "info",
            "w", "warn", "warning",
            "e", "err", "error"
        ]:
            if return == "TRUEFALSE":
                return False
            elif return == "NUMBER":
                return 0
            elif return == "YESNO":
                return "No"
        logFile = open("log.log", "a")
        time = str(datetime.datetime.now())
        #   123456789ABCDEFGHIJKLMNOPQ
        # * 2009-01-06 15:08:24.789150
        #   0123456789ABCDEFGHIJKLMNOP
        logFile.write("\n" + "[" + str(time[:19]) +
                      " " + type.upper() + "] " + text)
    except:
        if return == "TRUEFALSE":
            return False
        elif return == "NUMBER":
            return 0
        elif return == "YESNO":
            return "No"
    else:
        if return == "TRUEFALSE":
            return True
        elif return == "NUMBER":
            return 1
        elif return == "YESNO":
            return "Yes"
    finally:
        logFile.close()


if __name__ == '__main__':
    print(log("I", "Never gonna give you up!", "TRUEFALSE"))
    print(log("W", "Never gonna let you down!", "NUMBER"))
    print(log("E", "Never gonna run around and desert you!", "YESNO"))
    print(" \nCovered Software is provided under this License on an \"as is\" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the Covered Software is free of defects, merchantable, fit for a particular purpose or non-infringing. The entire risk as to the quality and performance of the Covered Software is with You. Should any Covered Software prove defective in any respect, You (not any Contributor) assume the cost of any necessary servicing, repair, or correction. This disclaimer of warranty constitutes an essential part of this License. No use of any Covered Software is authorized under this License except under this disclaimer. \n")
    print("\nSorry, but the logcreator is not a (G)UI project!")
    while True:
        notImportant = datetime.datetime.now()
