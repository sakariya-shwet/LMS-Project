# funamental booster

#<<<welcome section>>>>

print("Welcome to interactive data colletor")

print("\n This will collect your personal info")

print("\n give some calulation,and show you data type details.")

print("\n so, let's Begin in !!")



#<<<<collect info section>>>>

name=input("Enter your name:-")

age_str=input("Enter your age:-")

age=int(age_str)

height_str=input("Enter your height in meters:-")

height=float(height_str)

fav_num_str=input("Enter your fav num:-")

fav_num=int(fav_num_str)



#<<<<data processing>>>>

print("\n" + "=" * 30)

print("Processing your data")

print("\n" + "=" * 30)


#<<<<calculate birth year>>>>

cur_year=2026

birth_year=cur_year-age

height_cm=height*100


#<<<<perform some arithmetic operation>>>>

sum_value=age + fav_num

product_value=age*fav_num

#<<<<type conversion>>>>

height_as_int=int(height)

age_as_float=float(height)

age_as_str=str(height)


#<<<<display result>>>>


print("\n" + "=" * 30)

print("Thank you! for you here is the info we collected:")

print("\n" + "=" * 30)


#<<<<display each variable with its type and memory>>>>

print(f"\n variablr details:")

print(f"name:{name} ->type{type(name)} -> Adress:{id(name)}")

print(f"age:{age} ->type{type(age)} -> Adress:{id(age)}")

print(f"height:{height} ->type{type(height)} -> Adress:{id(height)}")

print(f"fav_num:{fav_num} ->type{type(fav_num)} -> Adress:{id(fav_num)}")


#<<<<display conversion>>>>

print("\n" + "=" * 30)

print("Type conersion")

print("\n" + "=" * 30)

print(f"\n height as int:{height_as_int}->type:{type(height_as_int)}")

print(f"\n Age as float:{age_as_float}->type:{type(age_as_float)}")

print(f"\n age_as_str:{age_as_str}->type:{type(age_as_str)}")


#<<<<display operation>>>>

print("\n" + "=" * 30)

print("Calculated results:")

print("\n" + "=" * 30)

print(f"\n your height in cm:{height_cm}cm")

print(f"\n Approximately birth year:{birth_year}")

print(f"\n sum of your age and fav_num:{sum_value}")

print(f"\n product of your age and fav_num:{product_value}")


#<<<<str concatination>>>>

greeting ="Hello , "+name+"!"

message=(f" ->'{greeting}'")

print(f" type:{type(greeting)}")

print(f" adress:{id(greeting)}")

print(f" :'{message}'")

print(f" type:{type(message)}")

print(f" Adress:{id(message)}")


#<<<<summary Table>>>>

print("\n" + "=" * 30)

print("Thank you for using the personal data collector!!")

print("\n" + "=" * 30)

print("\n you have successfully explore:")

print("\n input() and print() functions:")

print("\n str,int and float data types:")

print("\n Arithmetic operation (+,-,*,/),")

print("\n type() and id() built in functions")

print("str concatination")

print("Type casting")

print("\n" + "=" * 30)










