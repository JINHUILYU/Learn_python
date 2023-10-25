# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        left_count = mergeSort(left_half)
        right_count = mergeSort(right_half)

        # Merge both halves and count significant inversions
        i = j = k = count = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > 2 * right_half[j]:
                count += len(left_half) - i
                j += 1
            else:
                i += 1

        arr[:] = sorted(arr)
        return left_count + right_count + count

    return 0


# Example usage
arr = [1, 20, 6, 4, 5]
print(mergeSort(arr))  # Output: 3

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
