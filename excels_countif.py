def get_criteria(criteria):
    if type(criteria) is not str:
        return '==' + str(criteria)
    if criteria[0] not in ['>', '<']:
        return '=="' + criteria + '"'
    return criteria


def count_if(values, criteria):
    count = 0
    criteria = get_criteria(criteria)
    for value in values:
        if type(value) is str:
            value = '"' + value + '"'
        if eval(str(value) + criteria):
            count += 1
    return count


def sum_if(values, criteria):
    count = 0
    criteria = get_criteria(criteria)
    for value in values:
        if eval(str(value) + criteria):
            count += value
    return count


def average_if(values, criteria):
    count, the_sum = 0, 0
    criteria = get_criteria(criteria)
    for value in values:
        if eval(str(value) + criteria):
            count += 1
            the_sum += value
    return float(the_sum) / (count or 1)
