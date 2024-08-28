import sys
import os


def replaceAndPrintResult(conf_path: str, data_path: str) -> None:
    """Replacing matches in text and print result in console
    :param conf_path: path to configuration file
    :param data_path: path to data file
    """
    replaceConfig = getConfValues(conf_path)
    replaceData = getText(data_path)
    infoAboutReplace = replaceMathesAndCount(replaceConfig, replaceData)
    sortAndPrint(infoAboutReplace)


def getConfValues(conf_path: str) -> dict:
    """Get information about substitutions from a given configuration file
    :param conf_path: path to configuration file
    :return: dictionary with substitution data
    """
    substitutionConf = {}
    with open(conf_path, 'r') as file:
        lines = [line.strip() for line in file]
        for line in lines:
            splittedLine = line.split('=', 1)
            substitutionConf[splittedLine[0]] = splittedLine[1]
    return substitutionConf


def getText(data_path: str) -> list:
    """Get information about text from a given data file
    :param data_path: path to data file
    :return: list with text data
    """
    data = []
    with open(data_path, 'r') as file:
        lines = [line.strip() for line in file]
        for line in lines:
            data.append(line)
    return data


def replaceMathesAndCount(conf: dict, data: list) -> dict:
    """
    :param conf: configuration data
    :param data: text data
    :return: dictionary with changed lines and count of substitution
    """
    modifiedLineAndCount = {}
    for line in data:
        count = 0
        for key in conf.keys():
            count += line.count(key)
            line = line.replace(key, conf.get(key))
        modifiedLineAndCount[line] = count
    return modifiedLineAndCount


def sortAndPrint(substitutionData: dict) -> None:
    """Sort and output resulting text to console
    :param substitutionData: dictionary with changed lines and count of substitution
    """
    sortDict = sorted(substitutionData.items(), key=lambda x: x[1], reverse=True)
    for i in sortDict:
        print(i[0])


if __name__ == "__main__":
    if len(sys.argv) == 3:
        if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
            replaceAndPrintResult(sys.argv[1], sys.argv[2])
        else:
            print("One of the files does not exist, check the paths")
    else:
        print('Usage: ConfigReplacement.py {config_path} {text_path}')