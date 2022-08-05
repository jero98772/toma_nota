import re
txt = "hello planet ,hehho heaeeeeeeee-92ellllo-2 542fg -4 estrdt-jyhkj -222224555 -0"
x = re.findall("-\d*", txt)
print(x)
