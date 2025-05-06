import parser
import codecs

f = codecs.open("C:\\Users\\dedey\\OneDrive\\Рабочий стол\\LR1.txt", "w+", encoding="utf-8")
for item in parser.parse():
    f.write(item.find("h3").text + "\n")
f.close()