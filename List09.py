def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    x = 1
    while x < len(list1):
        if list1[0] == list1[x]:
            return True
        else:
            return False
    x+=1
print(main([1, 1, 1, 1, 1]))