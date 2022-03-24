import math  # 用pi,sin,cos ...

a = 10
print(type(a))

b = 20
a, b = b, a  # swap
print(a, b)

# 加(+),減(-),乘(*),除_float(/),除_int(//),mod(%),次方(**)

a = math.pi  # a=3.14...
a = math.e
a = math.sqrt(4)  # a = 根號 4

# 請算出⼀一年年365天總共有幾秒，並將答案指派到
# sec_per_year這個變數，並且印出
sec_per_year = 60 * 60 * 24 * 365
print(sec_per_year)

# 請算出⼀一個半徑為 3公尺的圓，其面積為何? 將答
# 案指派到 circle_area 這個變數並印出。
circle_area = 3 ** 2 * math.pi

# 算出你生日年月日數字總和(e.g. 1998+5+12)，
# 並求平方根，輸出總和與其平方根。
bdaysum = 2001 + 10 + 4
sqrt_sum = math.sqrt(bdaysum)
print(bdaysum, sqrt_sum)

# 請使用者輸入，將輸入公里轉換成英哩並輸出 (1
# 公里=0.62英哩)。
mile = 0.62 * float(input("enter kilometer : "))
print(mile)

# • 請使用者輸入，將輸入的攝氏溫度轉換成華氏溫
# 度並輸出。
# 攝氏=(華氏-32)*5/9。
F = (float(input("please enter temperature(C) : "))) * 9 / 5 + 32
print(F)

# 撰寫一個程式，讓使用者輸入一個數字並計算
# 其log值且印出。(提示：可用 math.log10函式
print(math.log10(float(input("enter int : "))))

# 請撰寫一個程式，讓使用者輸入兩兩個數字x與y，並計
# 算xy次方值且印出。
x = float(input("x : "))
y = float(input("y : "))
print(x ** y)

# 請撰寫一個程式，讓使用者輸入民國年年份並轉換成西元
# 年份印出。
print(1911 + float(input("enter year : ")))

# 請撰寫一個程式，讓使用者輸入一個角度並計
# 算其sin值且輸出。(提示: 利利用數學函數sin()，
# sin()裡需為弧度，角度轉成弧度公式為
# radians  = degrees * PI / 180)
degree_in = float(input("enter degree : "))
print(math.sin(degree_in * math.pi / 180))

# 可以將其他資料形態轉成字串串: str()
a = 1
print(type(str(a)))

# 字串串結合: +
a = 'qwe'
b = 'ewq'
print(a + b)

# 字串串複製: *
print(a * 3)

# 字串互換
x = 'this is apple'
y = 'Hello! Python!'
print(x)
print(y)
x, y = y, x
print(x)
print(y)

s = 'abc'
print(s[0], s[-1])  # first=0,last=-1

# Python字串串是不可變的
# e.g. s='this' 不能s[0]=g變成ghis

s = '1234567890'
s2 = s[0:5]
print(s2)  # 12345
s3 = s[0:8]
print(s3)  # 12345678
s4 = s[0:9:2]
print(s4)  # 13579
s4 = s4[::-1]  # 97531#reverse
print(s4)

# string.split('__')用__分割string
s = 'qwe qwe qwe'
print(s.split(' '))#變['qwe'],['qwe'],['qwe']
s = s.split(' ')
print(len(s))

s='1234567890'
print(s[0:6])#123456
print(s[6])#7

# use join() to combine split string
s = '-'.join(s)
print(s)

# str.replace(from,to)
s = s.replace('-', 'c')
print(s)

str1 = 'qwe ssd zxc rt poi lkj iu'
str1 = str1.split(' ')  # 用空格隔開
print(str1)#list
print(len(str1))
str1 = 'pp'.join(str1)  # 隔開的地方塞'pp'
print(str1)
print(str1.startswith('qwe'))  # 是否為'qwe'開頭
print(str1.find('rt'))  # 找第一個位置 rfind最後一個
print(str1.upper())  # 轉大寫

s = 'Knowledge is one thing virtue is another good sense is not conscience refinement is not humility nor is largeness and justness of view faith Philosophy however enlightened however profound gives no command over the passions no influential,motives,no,vivifying,principles Liberal Education makes not the Christian not the Catholic but the gentleman It is well to be a gentleman it is well to have a cultivated intellect a delicate taste a candid equitable dispassionate mind a noble and courteous bearing in the conduct of life these are the connatural qualities of a large knowledge they are the objects of a University. I am advocating I shall illustrate and insist upon them but still I repeat they are no guarantee for sanctity or even for conscientiousness and they may attach to the man of the world to the profligate to the heartless pleasant alas and attractive as he shows when decked out in them.'

s = s.split(' ')
print(s)
print(len(s))
print(s[65])
print('intelligence' in s)  # if iss inside => 1
print(s.index('Philosophy'))  # print the index
s2 = 'my student id is 1093324'
s.append(s2)
print(s)
a = s.index('influential,motives,no,vivifying,principles')
sp = s[a].split(',')  # sp變成[['influential'],['motives']...]#兩層
s[a] = sp  # 放回原位
print(s)
b = s.index(sp)
print(s[b][1])  # motives

mylist = ['a', 'b', 'c', 'd', 'e']
b = ['f', 'g', 'h']
mylist.append(b)
print(mylist)  # ['a', 'b', 'c', 'd', 'e', ['f', 'g', 'h']]#放整個物件
mylist.extend(b)
print(mylist)  # ['a', 'b', 'c', 'd', 'e', ['f', 'g', 'h'], 'f', 'g', 'h']#放各個元素

l = ['a', 'b', 'c']
# l.insert(2, 'r')#在l[2]插入'r'#原l[1],l[2]變l[1],l[3]
print(l)  # a,b,r,c
del l[0:2]#刪掉前兩個
print(l)#r,c
l2 = [1, 2, 5, 7, 3, 6, 9, 3, 7]
print(sorted(l2))
print(l2)
l2 = [1, 2, 5, 7, 3, 6, 9, 3, 7]
print(l2)
l2.sort()
print(l2)

score = [33, 100, 99, 45, 77, 35, 100, 12, 100, 99, 45]
sort_score = sorted(score, reverse=1)  # 大到小
b = [59, 34, 10, 88, 90]
sort_score.extend(b)
sort_score = sorted(sort_score, reverse=1)
print(sort_score)
n = sort_score.index(59)  # pass the index of the element
sort_score[n] = 60  # 直接用index去改
print(sort_score)

art_str = 'k,n,o,w,l,e,d,g,e,i,s,o,n,e,t,h,i,n,g,v,i,r,t,u,e,i,s,a,n,o,t,h,e,r,g,o,o,d,s,e,n,s,e'
ml = art_str.split(',')
print(ml.count('e'))  # 數有幾個'element'
name = 'eason'
ml.append(name)
print(ml)
del ml[0:8]
print(ml)
ml.insert(0, 'z')
print(ml)
ml = sorted(ml, reverse=1)
print(ml)
n = ml.index('a')  # find a's index
del ml[n]  # delete it
print(ml)
