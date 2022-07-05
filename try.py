# number = int(input("Tell number:"))
# for i in range(1,11):
#     print("It is a {} multiplication table".format(number))
#     for j in range(1,11):
#         print("{} x {} = {}".format(number,j,number * j))

# print factorial of number

# number = int(input("Enter number and it will return foctorial of that number:\n"))
# factorial = 1
# if number < 0:
#     print("Factorila dosn't have negative number")
# elif number < 2:
#     print("{} x {}".format(number, factorial))
# else:
#     for num in range(number,1,-1):
#         factorial = factorial * num
#     print("{}! = {} ".format(number, factorial))

# print factorial of number
# n = int(input("enter number:\n"))
# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         n = n *fact(n-1)
#         return n
# print("The factorial of",n,"is",fact(n))


#while loop
# count = 0
#
# while count < 9:
#     print("Number: ", count)
#     count = count + 1

# import tabula
# df = tabula.read_pdf(r'data/a.pdf', pages = 'all',multiple_tables=[1])[1]
# df.to_excel(r'data/22.xlsx')

# import tabula
# pdf_path = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"
#
# dfs = tabula.read_pdf(pdf_path, stream=True)
# # read_pdf returns list of DataFrames
# print(len(dfs))
# dfs[0]

#
# def my_function(a,b = 0):
#     c = a + b
#     return c
# help(my_function)
# print(my_function.__doc__)

# my_list = [[1], [2, 3], [4, 5, 6, 7]]
#
# flat_list = []
# for sublist in my_list:
#     for num in sublist:
#         flat_list.append(num)
#
# print(flat_list)


# 3. Write a Python program to flatten a given nested list structure.
# def flatten_list(_2d_list):
#     flat_list = []
#     # Iterate through the outer list
#     for element in _2d_list:
#         if type(element) is list:
#             # If the element is of type list, iterate through the sublist
#             for item in element:
#                 flat_list.append(item)
#         else:
#             flat_list.append(element)
#     return flat_list
#
# nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# print('Original List', nested_list)
# print('Transformed Flat List', flatten_list(nested_list))


# x = input("Enter any sentence:")
# y = x.split(' ')
# r = y[::-1]
# z = ' '.join(r)
#
# print(z)

# def my_function(x):
#     return x[::-1]
#
# mytxt = my_function(input(" tell"))
#
# print(mytxt)

#remove dup. elementd
# def remove_dup_items():
#     a = [10,20,30,40,10]
#     for i in a:
#         if a.count(i)>1:
#             a.remove(i)
#             return a
# print(remove_dup_items())


#print common values only
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3,4]
# lst = []
#
# for i in lst1:
#     if i in lst2:
#         lst.append(i)
# print(lst)

# 3. Write a Python program to flatten a given nested list structure.
# def flatten_list(_2d_list):
#     flat_list = []
#     for element in _2d_list:
#         if type(element) is list:
#             for item in element:
#                 flat_list.append(item)
#         else:
#             flat_list.append(element)
#     return flat_list
#
# nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# print('Original List', nested_list)
# print('Transformed Flat List', flatten_list(nested_list))

# Write a Python program to flatten a given nested list structure.
# nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# f_lsit = []
# for i in nested_list:
#     for j in i:
#         f_lsit.append(j)
# print(f_lsit)


# class Vehicle:
#     def __init__(self, w_amount, name):
#         self.w_amount = w_amount
#         self.name = name
#
# class Car(Vehicle):
#     def __init__(self, model, date, w1_amount, name ):
#         super().__init__(w_amount=w1_amount, name=name)
#         self.w1_amount = w1_amount
#         self.model = model
#         self.date = date
#
#
# Car_= Car(w1_amount = 4, name = "BMW", model= "12", date= "222")
# print(Car_.date)
# print(Car_.w1_amount)

class country:
    def __init__(self,name,continent):
        self.name = name
        self.continent = continent
    def name_country(self):
        return " The name is {} and the continent is {}".format(self.name,self.continent)

class brand():
    def __init__(self,brand_name,business_start_date ):
        self.brand_name = brand_name
        self.business_start_date = business_start_date
    def brand_business_start_date(self):
        return "The brand name is {} and the business start date is {}".format(self.brand_name,self.business_start_date)

class Season():
    def __init__(self, season_name, average_temperature):
        self.season_name = season_name
        self.average_temperature = average_temperature
    def season_avg_temp(self):
        return "The season name is {} and average temperature is {}".format(self.season_name,self.average_temperature)

class Product(country,brand,Season):
    def __init__(self,name,continent,brand_name,business_start_date,season_name,average_temperature,product_name,product_type,product_price,product_quantity):
        super().__init__(name,continent,brand_name,business_start_date,season_name,average_temperature)
        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price
        self.product_quantity = product_quantity
    def product_name_type_price_quantity(self):
        return "The product name is {}, the product type is {}, the product price {}, the product quantity is {}".format(self.product_name, self.product_type, self.product_price,self.product_quantity)


# ac = brand("WY", 2021)
# print(ac.brand_business_start_date())
#
# ac = country("Armenia", "Yerevan")
# print(ac.name_country())
#
# season_tem = Season("Summer",40)
# print(season_tem.season_avg_temp())


# cbs =  Product ("Wes", "Shoes", 20000000, "High premium")
cbs =  Product("WY", 2021, "Armenia", "Yerevan", "Summer",40, "Wes", "Shoes", 20000000, "High premium")
print(cbs.product_name_type_price_quantity())


