from time import sleep, time
from Bars import Bars

def setup(array):
    array.setup()
    array.moves = 0
    array.start = time()
    for bar in array:
        bar.active = False

    array.update()


def update(array, index):
    array[index].active = True
    array.update()
    array.moves += 1
    array[index].active = False


def finish(array, sleep_time=0.0):
    N = len(array)
    for i in range(N):
        try:
            array[i].active = True
            array.update()
            sleep(sleep_time)
        except:
            pass


def bubble_sort(array, start=0, end=-1):
    setup(array)
    N = len(array)

    start = start % N
    end = end % N

    for i in range(N):
        for j in range(N - i - 1):
            update(array, j)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            sleep(array.sleep_time)
    finish(array, array.sleep_time)


def insertion_sort(array, start=0, end=-1):
    setup(array)
    N = len(array)

    start = start % N
    end = end % N

    for i in range(1, N):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            update(array, j)
            array[j + 1] = array[j]
            j -= 1
            sleep(array.sleep_time)
        array[j + 1] = key
    finish(array, array.sleep_time)


def selection_sort(array, start=0, end=-1):
    setup(array)
    N = len(array)

    start = start % N
    end = end % N

    for i in range(N):
        min_index = i
        for j in range(i + 1, N):
            update(array, j)
            if array[min_index] > array[j]:
                min_index = j
            sleep(array.sleep_time)
        array[i], array[min_index] = array[min_index], array[i]
    finish(array, array.sleep_time)


def quick_sort(array):
    def partition(array, low, high):
        i = low - 1
        pivot = array[high]
        for j in range(low, high):
            update(array, j)
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
            sleep(array.sleep_time)
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quick_sort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quick_sort(array, low, pi - 1)
            quick_sort(array, pi + 1, high)

    setup(array)
    quick_sort(array, 0, len(array) - 1)
    finish(array, array.sleep_time)


def cycle_sort(array):
    setup(array)
    writes = 0
    N = len(array)
    for cycle_start in range(0, N - 1):
        item = array[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, N):
            update(array, i)
            if array[i] < item:
                pos += 1
            sleep(array.sleep_time)
        if pos == cycle_start:
            continue
        while item == array[pos]:
            pos += 1
        array[pos], item = item, array[pos]
        writes += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, N):
                update(array, i)
                if array[i] < item:
                    pos += 1
                sleep(array.sleep_time)
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            writes += 1
    finish(array, array.sleep_time)


def shell_sort(array, parameter=3):
    setup(array)
    N = len(array)
    h = 1
    while h < N / parameter:
        h = parameter * h + 1
    while h >= 1:
        for i in range(h, N):
            update(array, i)
            j = i
            while j >= h and array[j - h] > array[j]:
                array[j], array[j - h] = array[j - h], array[j]
                j -= h
                sleep(array.sleep_time)
        h = h // parameter
    finish(array, array.sleep_time)


def heap_sort(array):
    def heapify(array, N, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < N and array[index] < array[left]:
            largest = left
        if right < N and array[largest] < array[right]:
            largest = right
        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            update(array, index)
            sleep(array.sleep_time)
            heapify(array, N, largest)

    setup(array)
    N = len(array)
    for i in range(N // 2 - 1, -1, -1):
        heapify(array, N, i)
    for i in range(N - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    finish(array, array.sleep_time)


def merge_sort(array):
    def merge(array, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = Bars([0] * (n1),array.x, array.y, array.width, array.height)
        R = Bars([0] * (n2),array.x, array.y, array.width, array.height)
        for i in range(0, n1):
            L[i] = array[l + i]
        for j in range(0, n2):
            R[j] = array[m + 1 + j]
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            update(array, k)
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
            sleep(array.sleep_time)
        while i < n1:
            update(array, k)
            array[k] = L[i]
            i += 1
            k += 1
            sleep(array.sleep_time)
        while j < n2:
            update(array, k)
            array[k] = R[j]
            j += 1
            k += 1
            sleep(array.sleep_time)

    def merge_sort(array, l, r):
        if l < r:
            m = l + (r - l) // 2
            merge_sort(array, l, m)
            merge_sort(array, m + 1, r)
            merge(array, l, m, r)

    setup(array)
    merge_sort(array, 0, len(array) - 1)
    finish(array, array.sleep_time)


def radix_sort(array, base=10):
    setup(array)
    N = len(array)
    max1 = max(array)
    exp = 1
    while max1 // exp > 0:
        output = Bars([0] * N, array.x, array.y, array.width, array.height)
        count = Bars([0] * base, array.x, array.y, array.width, array.height)
        for i in range(N):
            index = array[i] // exp
            count[index % base] += 1
        for i in range(1, base):
            count[i] += count[i - 1]
        i = N - 1
        while i >= 0:
            index = array[i] // exp
            output[int(count[index % base] - 1)] = array[i]
            count[index % base] -= 1
            i -= 1
        for i in range(N):
            array[i] = output[i]
            update(array, i)
            sleep(array.sleep_time)
        exp *= base
    finish(array, array.sleep_time)


def count_sort(array):
    setup(array)
    N = len(array)
    output = Bars([0] * N, array.x, array.y, array.width, array.height)
    MAX = int(max(array))+1
    MIN = int(min(array))-1
    count = [0] * (MAX-MIN+1)
    for i in range(N):
        count[int(array[i]) - MIN] += 1
    for i in range(MIN, MAX+1):
        count[i - MIN] += count[i - 1 - MIN]
    i = N - 1
    while i >= 0:
        output[count[int(array[i]) - MIN] - 1] = array[i]
        count[int(array[i] - MIN)] -= 1
        i -= 1
    for i in range(N):
        array[i] = output[i]
        update(array, i)
        sleep(array.sleep_time)
    finish(array, array.sleep_time)