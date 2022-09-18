#Lab7.3 Comb Sort

def comb_sort(data):
    shrink_factor = 1.3
    gap = len(data)
    swapped = True
    i = 0

    while gap > 1 or swapped:
        # Update the gap value for a next comb
        gap = int(float(gap) / shrink_factor)

        swapped = False
        i = 0

        while gap + i < len(data):
            if data[i] > data[i+gap]:
                # Swap values
                data[i], data[i+gap] = data[i+gap], data[i]
                swapped = True
            i += 1

    return data


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(comb_sort(unsorted))
