# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def checkFileType(string):
    if string.endswith((".mp3", ".aac", ".flac")):
        return "music"
    elif string.endswith((".jpg", ".bmp", ".gif")):
        return "images"
    elif string.endswith((".mp4", ".avi", ".mkv")):
        return "movies"
    else:
        return "other"

def parserBytes(string):
    return int(string.replace("b", ""))

def solution(S):
    # write your code in Python 3.6
    stats = {
        "music": 0,
        "images": 0,
        "movies": 0,
        "other": 0,
        }
    for i in S.split("\n"):
        file, bytes = i.split(" ")
        # print(checkFileType(file), file, bytes)
        cate = checkFileType(file)
        data = stats.get(cate, 0)
        data += parserBytes(bytes)
        stats.update({cate: data})
    # print(stats)
    ret = ""
    for ftype in stats:
        ret += "{} {}b\n".format(ftype, stats[ftype])
    # print(ret)
    return ret