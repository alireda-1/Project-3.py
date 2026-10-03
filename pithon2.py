str_Tminutes=input("Please type the number of minutes:\n")

int_Tminutes=int(str_Tminutes)

int_hours=int_Tminutes//60
int_minutes=int_Tminutes%60

print("This course is : "+ str(int_hours) + 'hours and '+ str(int_minutes) +' minutes long')