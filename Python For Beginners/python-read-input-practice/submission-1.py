def add_two_numbers() -> int:
    input_string = input()
    list_string = input_string.split(",")
    nums = []
    for num in list_string:
        nums.append(int(num))
    
    return sum(nums)

    # return sum([int(num) for num in input().split(",")])



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
