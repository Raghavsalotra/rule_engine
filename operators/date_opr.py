from time import strptime

def less_than_equals(source, target):
    src_date = source.replace('_', ' ')
    src_date = strptime(src_date, '%Y-%m-%d %H:%M:%S')
    trg_date = strptime(target['value'], '%Y-%m-%d %H:%M:%S')

    if src_date <= trg_date:
        return True

    return False


def greater_than_equals(source, target):

    src_date = source[2].replace('_', ' ')
    src_date = strptime(src_date, '%Y-%m-%d %H:%M:%S')
    trg_date = strptime(target['value'], '%Y-%m-%d %H:%M:%S')

    if src_date >= trg_date:
        return True

    return False

