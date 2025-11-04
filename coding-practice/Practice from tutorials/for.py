# exp = [2300,4000,3400,4500,2000]
# # total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
# total = 0
# for item in exp:
#     total = total + item
# print(total)




# Even Number
# a = int(input("Enter a number: "))
# for i in range(1,a):
#     if i % 3 == 0:
#       print(i)



#Monthly Expense


# exp = [2300,4000,3400,4500,2000]
# total = 0
# for i in range(0,5):
#     print('Month:',(i+1),'Expense:',exp[i])
#     total = total+exp[i]
# print(total)


#Location found

# key = "Chair"
# Location = ["Room","Bed Room","Chair","Bed"]
# for i in Location:
#     if i == key:
#         print("Key is Found",i)
#         break
#     else:
#         print("Key not Found",i)



#Skip the numbers

for i in range(0,6):
    if i%2 == 0:
        continue
    print(i*i)