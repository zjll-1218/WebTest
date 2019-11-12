import os


def getDir():
    """
    :return:获取最后修改的目录
    """
    runDirs = [d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('TestRun')]
    latestDir = max(runDirs, key=os.path.getmtime)
    return latestDir
