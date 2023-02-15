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