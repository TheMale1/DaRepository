def check_factor(big_num, small_num):
    return big_num % small_num == 0


# Main Routine
big = int(input("Enter the bigger number: "))
small = int(input("Enter the smaller number: "))
if check_factor(big, small):
    print(f"{small} is a factor of {big}")
else:
    print(f"{small} is not a factor of {big}")

