str_length=input("please type length :\n")
str_width=input("please type width :\n")
str_cost=input("how much for 1 meter? :\n")
#سأحول كل المعطيات الى فلوت لأتمكن من الحساب
length=float(str_length)
width=float(str_width)
float_cost=float(str_cost)
#لايجاد المساحة سأقوم بضرب الطول بالعرض وبعدها احول الناتج من فلوت الى سترينج لكي اتمكن من وضعه بعد + في الامر برينت
float_area=(length*width)
area=str(float_area)
print("The total area is:"+area)
#الأن سأحسب التكلفة وهي ضرب التكلفة للمتر بالمساحة وسأحولهم الى سترينج بنفس السطر
cost=str(float_cost*float_area)
print("Give the guy : $"+cost)