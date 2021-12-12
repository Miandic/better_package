import warnings
import threading
import json
from Parser.Companies.ParserCDEK import ParserCDEK
from Parser.Companies.ParserDHL import ParserDHL
from Parser.Companies.ParserDEL import ParserDEL
from Parser.Companies.ParserDPD import ParserDPD
from app import send_data


def parse(send_data):
    city_from = send_data[0]
    city_to = send_data[1]
    length = send_data[2]
    width = send_data[3]
    high = send_data[4]
    weight = send_data[5]
    cost = send_data[6]

    warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

    # self, start_point, end_point, currency, length , weight, height, width ,  money
    a = ParserDEL(city_from, city_to, "rub", length, weight, high, width, cost)
    b = ParserDHL(city_from, city_to, "rub", length, weight, high, width, cost)
    c = ParserCDEK(city_from, city_to, "rub", length, weight, high, width, cost)
    d = ParserDPD(city_from, city_to, "rub", length, weight, high, width, cost)

    write_CDEK = threading.Thread(target=a.write_data)
    write_DHL = threading.Thread(target=b.write_data)
    write_DEL = threading.Thread(target=c.write_data)
    write_DPD = threading.Thread(target=d.write_data)

    write_CDEK.start()
    write_DHL.start()
    write_DEL.start()
    write_DPD.start()

    write_CDEK.join()
    write_DHL.join()
    write_DEL.join()
    write_DPD.join()

    post_data = [a.returned_data, b.returned_data, c.returned_data, d.returned_data]
    x = {
        "a": a.returned_data, "b": b.returned_data, "c": c.returned_data, "d": d.returned_data
    }
    with open("data.json", "w") as write_file:
        json.dump(x, write_file)

    j = {
        "a": 1
    }
    with open("flag.json", "w") as write_file:
        json.dump(j, write_file)
    # data = json.dumps(x)
    return post_data
