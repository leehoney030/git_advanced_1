from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list. [cite: 9]

    Args:
        int_list: A list of integer. [cite: 9]

    Returns:
        A list of even integers. [cite: 9]
    """
    #TODO: Implement even_list [cite: 9]
    temp = []
    for num in int_list:
        if num % 2 == 0:
            temp.append(num)
    return temp

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list of integers. [cite: 11]

    Args:
        even_int_list: A list of even integers. [cite: 11]

    Returns:
        The sum of the squares of all even numbers in the list. [cite: 12]
    """
    #TODO: Implement sum_of_squares_of_even [cite: 13]
    pass

#Main function
def main():

    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_int_list = even_list(int_list)

    output = sum_of_squares_of_even(even_int_list)

    print(output)

# Boilerplate code
if __name__ == "__main__":

    main()