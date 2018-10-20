def is_isogram(string):
    if isinstance(string,str):
        for i in string:
            if string.count(i) == 1 or string == "":
                return string, True
            else:
               return string, False
    else:
        raise Exception("not string")