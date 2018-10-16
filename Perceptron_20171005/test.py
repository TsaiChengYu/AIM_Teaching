#encoding:UTF-8

x=1+2
print(x)

y = 2.0+3.1
print(y)

print(x+y)

z1=(2==3)
z2=(False)
print(z1)
print(z2)

a=(3 + 2j)
b=(1+ 3j)

print(a+b)
print(a*3)

#----------------------------------------------
# String Type
x = "Hello, World"
y="jeffery"
print(x+y)
print(x[1])

# Container Type
x = [1,2,3]
print(type(x))

x={1,2,3}
print(type(x))

x={"a":1,"b":2,"c":3}
print(x["a"])
print(type(x))

#------------if# ----------------------------------
a= 10
if(a>=300):
    print("a>300")
elif(a>=200):
    print ("a>200")
else:
    print ("a<200")

#------------for ----------------------------------
a= 10
for i in range(a):
    print (i)

#------------for ----------------------------------
Temperature = input("現在氣溫：")
if (float(Temperature) > 28):        #若氣溫高於28度
        print("氣溫>28度，可開啟冷氣。")
elif (int(Temperature) < 16):        #若氣溫低於16度
        print("氣溫<16度，可開啟暖氣。")
else:
    #若氣溫非高於28度也非低於16度
        print("氣溫舒適，請避免開啟冷/暖氣機。")

#------------test----------------------------------
Height = input()
Weight = input()
BMI = float(Weight) / (float(Height)/100)**2
print(BMI)

if (BMI < 18.5):
        print("BMI值為%.2f，屬體重過輕" % BMI)
elif (18.6 <= BMI and BMI < 24):
        print("BMI值為%.2f，屬正常範圍" % BMI)
elif (24 <= BMI and BMI < 27):
        print("BMI值為%.2f，屬稍重" % BMI)
elif (27 <= BMI and BMI < 30):
        print("BMI值為%.2f，屬輕度肥胖" % BMI)
elif (30 <= BMI and BMI < 35):
        print("BMI值為%.2f，屬中度肥胖" % BMI)
else:
        print("BMI值為%.2f，屬重度肥胖" % BMI)

