import re
s = """<div class='jack'><span id ='1'>天马星空</span></div>
<div class='jack'><span id ='1'>窈窕淑女</span></div>
<div class='jack'><span id ='1'>云中飞鸟</span></div>
"""

obj=re.compile(r"<div class=.*?><span id =.*?>(?P<name>.*?)</span></div>",re.S)
result=obj.finditer(s)
for it in result:
    print(it.group("name"))
    #re.S让.能够匹配换行符
    #(?p<name>.*?)      P要大写