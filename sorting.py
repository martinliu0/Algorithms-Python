#Sorting algorithms:
#    quick sort and merge sort
#Both implementations sort the list in place.
#
#I used the timeit module to test performance,
#quick sort in the best case takes about half the time of merge sort.
#However, neither implementation comes even close to the default sort().


#quick sort
def quick_sort(mylist):
    quick_sort_helper(mylist, 0, len(mylist)-1)

def quick_sort_helper(mylist, start, end):
    if start < end:
        midpoint = partition(mylist, start, end)
        quick_sort_helper(mylist, start, midpoint-1)
        quick_sort_helper(mylist, midpoint + 1, end)

def partition(mylist, start, end):
    pivot_val = mylist[start]

    left = start + 1
    right = end

    while True:
        while left <= right and mylist[left] <= pivot_val:
            left += 1
        while left <= right and mylist[right] >= pivot_val:
            right -= 1

        if left > right:
            break
        else:
            mylist[left], mylist[right] = mylist[right], mylist[left]

    mylist[start], mylist[right] = mylist[right], mylist[start]
    return right


#merge sort
def merge_sort(mylist):
    if len(mylist) > 1:
        i,j,k = 0,0,0
        left_list = mylist[:len(mylist)//2]
        right_list = mylist[len(mylist)//2:]
        merge_sort(left_list)
        merge_sort(right_list)
        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                mylist[k] = left_list[i]
                i += 1
            else:
                mylist[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            mylist[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            mylist[k] = right_list[j]
            j += 1
            k += 1

if __name__ == "__main__":
    import random, collections
    from timeit import timeit

    randlist = random.sample(range(5000), 1000)

    randlist1 = randlist.copy()
    randlist2 = randlist.copy()
    if randlist == randlist2 and randlist1 == randlist2:
        print("quick: {}".format(timeit("quick_sort(randlist)", setup="from __main__ import quick_sort, randlist", number = 1)))
        print("merge: {}".format(timeit("merge_sort(randlist1)", setup="from __main__ import merge_sort, randlist1", number = 1)))
        print("default: {}".format(timeit("randlist2.sort()", setup="from __main__ import randlist2", number = 1)))
