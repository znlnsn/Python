import re
#findall:匹配字符串中所有符合正则的内容
lst = re.findall(r"\d+","我的号码商店63728，我女朋友是289272638")
print(lst)
#findter:匹配字符串中所有的内容（返回的是迭代器）从迭代器中拿到内容需要.group()
#.group()不加会变成另一种显示
it =re.finditer(r"\d+","我的号码商店63728，我女朋友是289272638")
for i in it:
     print(i.group())

#search返回的是match对象，拿到数据需要.group()，只能拿到一个数据
s=re.search(r"\d+","我的号码商店63728，我女朋友是289272638")
print(s.group())
#match从头开始匹配，匹配不到就报错

#预加载，先写正则表达式
obj = re.compile(r"\d+")
ret = obj.findall("我的号码商店63728")
for it in ret:
  print(it.group())
