def promedio(numros):
    total = 0
    for n in numros:
        total += n
    return total / len(numros)

def main():
    nums = [2,4,6]
    print('lista', nums)
    print('promedio:', promedio(nums))

if __name__ == '__main__':
    main()