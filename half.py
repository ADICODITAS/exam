#code for file ,we have to make a program  in python that will take a file path as input and a delimiter what we will we using in the file to separate the numbers (integers),after that seprate the number from the file and 
# add all the numbers that were present in the file where will only one type of delimiter in the file    


deli=input("enter delimiter that you useed in the file")
filee=input("enter file path")
def sum_numbers_in_file(deli):
    total = 0
    with open(filee, 'r') as file:
        for i in file:
            numbers = i.strip().split(deli)
            print(numbers)
            for number in numbers:
                total += int(number)
    print(total)
sum_numbers_in_file(deli)
