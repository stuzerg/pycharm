digit_r = [11, 2, 9, 7, 155, 1, 3, 2]
#digit_row.insert(6,33)
print(digit_r)



le_ = len(digit_r)
print(le_)
count_  = 0

# int(len(digit_row)/2+1)
for j in range(1, int(len(digit_r))):
    for i in range (j, len(digit_r) - j + 1):
        count_ += 1
        if digit_r[i - 1] > digit_r[i]:
            digit_r[i], digit_r[i - 1] = digit_r[i - 1], digit_r[i]
        if digit_r[le_ - i]  < digit_r[le_ - i - 1]:
            digit_r[le_ - i], digit_r[le_ - i - 1] = digit_r[le_ - i - 1], digit_r[le_ - i]
        print(digit_r)



    print()
print(count_)
print(digit_r)
