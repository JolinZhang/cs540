def quickSort(list):
    # dont forget to check corner case
    if len(list) <= 1:
        return list
    # format -> [!variable(x) to store in list(first)! -> for x in xxx if xxxx]


    smaller = [x for x in list[1:] if x <= list[0]]
    larger = [x for x in list[1:] if x > list[0]]
    return quickSort(smaller) + [list[0]] + quickSort(larger)
    # list should be use '+' to cancatanate the subList
    # instead of return quickSort(smaller), [list[0]], quickSort(larger)
# Main function
if __name__ == '__main__':
    list = [2,5,4,1,12,5,2]
    print quickSort(list) #dont forget to print xxx

