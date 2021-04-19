import time
import random
import tkinter as tk
from tkinter import *
import threading

# This is a prototype, seeing numbers getting sorted in real time helps me visualize the algorithms better,
# This program is by far finished, this is just a concept
# I plan to have an OOP approach in the future

window = tk.Tk(className="Sorting Algorithms with NUMBERS")
window.geometry("1200x800")
window['bg'] = 'grey'

a_list = [i for i in range(20)]


def bubble_sort(nums):
    random.shuffle(nums)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                time.sleep(2)
                for output in range(1):
                    frame = Frame(window, width=150, height=5, padx=20, pady=5)
                    frame.grid(row=2, column=0, columnspan=7)
                    blank = Text(frame, wrap=WORD)
                    blank.pack()
                    blank.insert(END, nums)
                    blank.configure(state=DISABLED)
                swapped = True


def selection_sort(nums):
    random.shuffle(nums)

    for i in range(len(nums)):

        lowest_value_index = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        time.sleep(2)
        frame = Frame(window, width=150, height=5, padx=20, pady=5)
        frame.grid(row=2, column=0, columnspan=7)
        blank = Text(frame, wrap=WORD)
        blank.pack()
        blank.insert(END, nums)
        blank.configure(state=DISABLED)


def insertion_sort(nums):
    random.shuffle(nums)
    for i in range(1, len(nums)):

        item_to_insert = nums[i]

        j = i - 1

        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = item_to_insert
        time.sleep(2)
        frame = Frame(window, width=150, height=5, padx=20, pady=5)
        frame.grid(row=2, column=0, columnspan=7)
        blank = Text(frame, wrap=WORD)
        blank.pack()
        blank.insert(END, nums)
        blank.configure(state=DISABLED)


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    random.shuffle(nums)
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
        time.sleep(2)
        frame = Frame(window, width=150, height=5, padx=20, pady=5)
        frame.grid(row=2, column=0, columnspan=7)
        blank = Text(frame, wrap=WORD)
        blank.pack()
        blank.insert(END, nums)
        blank.configure(state=DISABLED)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    time.sleep(2)
    for output in range(1):
        frame = Frame(window, width=150, height=5, padx=20, pady=5)
        frame.grid(row=2, column=0, columnspan=7)
        blank = Text(frame, wrap=WORD)
        blank.pack()
        blank.insert(END, sorted_list)
        blank.configure(state=DISABLED)

    return sorted_list


def merge_sort(nums):
    random.shuffle(nums)
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        time.sleep(2)
        frame = Frame(window, width=150, height=5, padx=20, pady=5)
        frame.grid(row=2, column=0, columnspan=7)
        blank = Text(frame, wrap=WORD)
        blank.pack()
        blank.insert(END, nums)
        blank.configure(state=DISABLED)
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    random.shuffle(nums)

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


t1 = threading.Thread(target=lambda: bubble_sort(a_list))
t1.setDaemon(True)
t2 = threading.Thread(target=lambda: selection_sort(a_list))
t2.setDaemon(True)
t3 = threading.Thread(target=lambda: insertion_sort(a_list))
t3.setDaemon(True)
t4 = threading.Thread(target=lambda: heap_sort(a_list))
t4.setDaemon(True)
t5 = threading.Thread(target=lambda: merge_sort(a_list))
t5.setDaemon(True)
t6 = threading.Thread(target=lambda: quick_sort(a_list))
t6.setDaemon(True)


quit_button = tk.Button(window, text="Quit", command=window.destroy).grid(row=0, column=1, pady=10, padx=40)
merge_button = tk.Button(window, text="Merge Sort", command=lambda: t5.start()).grid(row=0, column=2, pady=10, padx=40)
bubble_button = tk.Button(window, text="Bubble Sort", command=lambda: t1.start()).grid(row=0, column=3,
                                                                                       pady=10, padx=40)
quick_button = tk.Button(window, text="Quick Sort", command=lambda: t6.start()).grid(row=0, column=4, pady=10, padx=40)
selection_button = tk.Button(window, text="Selection Sort", command=lambda: t2.start()).grid(row=0, column=5,
                                                                                             pady=10, padx=40)
insertion_button = tk.Button(window, text="Insertion Sort", command=lambda: t3.start()).grid(row=0, column=6,
                                                                                             pady=10, padx=40)
heap_button = tk.Button(window, text="Heap Sort", command=lambda: t4.start()).grid(row=0, column=7, pady=10, padx=40)

if __name__ == "__main__":
    window.mainloop()
