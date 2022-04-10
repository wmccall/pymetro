def safe_get(list, index, default):
    try:
        return list[index]
    except:
        return default