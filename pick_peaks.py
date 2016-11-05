"""Code Wars Kata.

https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python
"""


def pick_peaks(arr):
    """Return peaks and their positions in a dict."""
    return_dict = {'pos': [], 'peaks': []}
    for i, item in enumerate(arr):
        if i != 0 and i != len(arr) - 1:
            if item > arr[i - 1] and item > arr[i + 1]:
                return_dict['pos'].append(i)
                return_dict['peaks'].append(item)
            elif item > arr[i - 1] and item == arr[i + 1]:    # deal w/ plateau
                j = i + 1
                while j <= len(arr) - 2:
                    if arr[j + 1] > arr[i + 1]:
                        break
                    elif arr[j + 1] < arr[i + 1]:
                        return_dict['pos'].append(i)
                        return_dict['peaks'].append(item)
                        break
                    j += 1
    return return_dict
