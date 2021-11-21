from datetime import date
import itertools


def cnt_time(a, b):
    c = date.today()
    c = c.year
    a1 = list(map(str, a.split()))
    b1 = list(map(str, b.split()))
    if (c % 4 == 0 and c % 100 != 0):
        days = {"янв": 0, "фев": 31, "мар": 60, "апр": 91, "май": 121, "июн": 152, "июл": 182, "авг": 213, "сен": 244,
                "окт": 274,
                "ноя": 305, "дек": 335}
    else:
        days = {"янв": 0, "фев": 31, "мар": 59, "апр": 90, "май": 120, "июн": 151, "июл": 181, "авг": 212, "сен": 243,
                "окт": 273,
                "ноя": 304, "дек": 334}
    if (int(b1[0]) + days[b1[1]] >= int(a1[0]) + days[a1[1]]):
        return (int(b1[0]) + days[b1[1]] - int(a1[0]) - days[a1[1]])
    elif (c % 4 == 0 and c % 100 != 0):
        return (366 - int(a1[0]) - days[a1[1]] + int(b1[0]) + days[b1[1]])
    else:
        return (365 - int(a1[0]) - days[a1[1]] + int(b1[0]) - days[b1[1]])


def xpath_soup(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        previous = itertools.islice(parent.children, 0, parent.contents.index(child))
        xpath_tag = child.name
        xpath_index = sum(1 for i in previous if i.name == xpath_tag) + 1
        components.append(xpath_tag if xpath_index == 1 else '%s[%d]' % (xpath_tag, xpath_index))
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)
