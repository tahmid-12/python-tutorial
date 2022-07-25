def remove(arr, l1):
    # word = arr.strip()
    if l1 in arr:
        arr.remove(l1)
    return arr


r = remove(['tom','robert','chris','scarllet'],'robert')
print(r)