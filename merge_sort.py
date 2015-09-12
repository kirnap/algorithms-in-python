# Implementation of merge-sort algorithm is purely for educational purposes.

# This example is an intermediate for python learners and will be really helpful to better understand the programming
# and algorithm paradigm and highly recommended for python learners.
# Input is an list of any length and any entries and the output is a sorted version of a list


def merge(first, second):
	"""
	This function returns the merged version of first and second list object.
	Input lists has to be sorted in itself for example list1 = [3,5,64,7] where the integers listed in increasing order
	:param first:
	:param second:
	:return: ret
	"""
	i = 0
	j = 0
	ret = []
	# while loop is made for operation to be done until the total length of output is equal to sum of input lengths
	while len(ret) != len(first) + len(second):
		if i == len(first):  # this means that all the entries of first are appended to ret list and no need for comparison
			ret += second[j:]
		elif j == len(second):  # similarly all the entries of second list appended to the result list
			ret += first[i:]
		else:  # else statement compares two lists and then appends the smallest entry.
			if first[i] < second[j]:
				ret.append(first[i])
				i += 1
			else:
				ret.append(second[j])
				j += 1
	return ret


def merge_sort(iterable):
	"""
	Recursive call reduces until the base case which is the case of 1 entry in a list and then combines the two arrays
	and this operation is made until it reaches one single list

	Note that there is a python slice expression which partitions a list into two lists

	:param iterable:
	:return: Sorted version of array
	"""
	if len(iterable) == 1:
		return iterable
	else:
		left_part = iterable[:(len(iterable) / 2)]
		right_part = iterable[len(iterable) / 2:]
		result = merge(merge_sort(right_part), merge_sort(left_part))
	return result


if __name__ == '__main__':
	print merge_sort([1, 8, 7, 76, 9, 5, 2, 4])
