# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# Find the MAXIMUM sum of any k consecutive elements
arr = [2, 9, 5, 1, 3, 2]
k = 3
sum_slide = sum(arr[0:k])
max = sum_slide
for i in range(0,len(arr)):
    if i > k-1:
        sum_slide = sum_slide + arr[i]
        sum_slide = sum_slide - arr[i-3]
        if sum_slide> max:
            max =sum_slide
print(max)

    