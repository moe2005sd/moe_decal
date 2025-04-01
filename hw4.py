#Q2.1
num_list = list(range(21))  
print(num_list)  


#Q2.2
num_list = list(range(21))  

def square_List(list):  
    return [x**2 for x in list]  

squared_nums = square_List(num_list)  
print(squared_nums) 


#Q2.3
def first_fifteen_elements(list):  
    return list[:15]  

squared_nums = square_List(num_list)
print(first_fifteen_elements(squared_nums))  


#Q2.4
def every_fifth_element(list):  
    return list[4::5]

squared_nums = square_List(num_list)
print(every_fifth_element(squared_nums))  


#Q2.5
def fancy_function(list):  
    return list[::-3]

squared_nums = square_List(num_list)
print(fancy_function(squared_nums))  


#Q3.1
def create_2d_list():
    return [[j for j in range(i, i + 5)] for i in range(1, 26, 5)]

matrix = create_2d_list()
print(matrix)


#Q3.2
def modified_2d_list(matrix):
    return [['?' if num % 3 == 0 else num for num in row] for row in matrix]

matrix = create_2d_list()
print(modified_2d_list(matrix))


#Q3.3
def sum_non_question_elements(matrix):
    return sum(num for row in matrix for num in row if num != '?')

matrix = create_2d_list()
new_matrix = modified_2d_list(matrix)
print(sum_non_question_elements(new_matrix))