import warnings
import threading
from Parser.Companies.ParserCDEK import ParserCDEK
from Parser.Companies.ParserDHL import ParserDHL
from Parser.Companies.ParserDEL import ParserDEL

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# self, start_point, end_point, currency, length , weight, height, width ,  money
a = ParserDEL("Москва", "Ростов-на-Дону", "rub", "1", "2", "1", "1", "1500")
b = ParserDHL("Москва", "Ростов-на-Дону", "rub", "1", "2", "1", "1", "1500")
c = ParserCDEK("Москва", "Ростов-на-Дону", "rub", "1", "2", "1", "1", "1500")

write_CDEK = threading.Thread(target=a.write_data)
write_DHL = threading.Thread(target=b.write_data)
write_DEL = threading.Thread(target=c.write_data)

write_CDEK.start()
write_DHL.start()
write_DEL.start()

write_CDEK.join()
write_DHL.join()
write_DEL.join()
