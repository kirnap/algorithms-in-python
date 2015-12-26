"""
This is for an educational purposes
This is a good practice for intermediate python learners.

The definition of the problem: Suppose you are given a list of n elements with an arbitrary order and
you are asked to find the number of inversions in a given list by using Divide & Conquer Paradigm in computer science
Here is the definition of inversion: Number of pairs(i, j) of list indices i < j and List[i] > List[j]
for example it is given (2,3,5,6,1) the inversions are: (2,1) and (6,1)

Please note that you need a pen a piece of paper first to understand the problem and algorithm which also is explained
in https://class.coursera.org/algo-004/lecture/16?s=e
I highly recommend first to understand your algorithm in the paper and then get into the code!

"""


def sort_and_count(iterable):
    """
    This function recursively calls itself to break up the list into two parts and then recursively recover them
    the actual algorithm is implemented in this function

    """
    if len(iterable) == 1:
        return iterable, 0
    else:
        (sorted_left, left_inversion_number) = sort_and_count(iterable[:(len(iterable) / 2)])
        (sorted_right, right_inversion_number) = sort_and_count(iterable[len(iterable) / 2:])
        (result, split_inversion_number) = merge_and_count(sorted_left,sorted_right)
        return result,left_inversion_number + right_inversion_number + split_inversion_number


def find_inversions(iterable):
    """
    Since sort_and_count function returns a tuple and I just need the number of inversions first part is enough for
    me
    List:parameter
    Number:return
    """
    return sort_and_count(iterable)[1]


def merge_and_count(first, second):
    """
    It is explained during lecture that while implementing merge part there is a single path that
    counts the inversions automatically if the second part of the

    """
    i = 0
    j = 0
    ret = []
    number_of_inversion = 0
    while len(ret) != len(first) + len(second):
        if i == len(first):
            ret += second[j:]
        elif j == len(second):
            ret += first[i:]
        else:
            if first[i] < second[j]:
                ret.append(first[i])
                i += 1
            else:
                ret.append(second[j])
                j += 1
                number_of_inversion += len(first) - i
    return ret,number_of_inversion



