"""
첫 피봇은 arr[0]
arr의 앞에서 시작하는 left, 뒤에서 시작하는 right
피봇을 기준으로 이 두 값이 각각 작고 큰 값을 찾다가
찾으면 두 값을 서로 바꿔주고
못찾고 left와 right가 교차해버리면
right와 피봇값을 바꿔주어, 정렬중인 배열의 left와 right 중간에
그러니까, 피봇이 있어야 할 자리에 피봇을 넣어준다
partition 함수를 통해 피봇값을 얻고
quick_sort 함수를 통해 계속해서 분할하여 정복하는 식으로 배열을 정렬해나간다
"""

def partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(arr, left, right):
    if left < right:
        center = partition(arr, left, right)
        quick_sort(arr, left, center-1)
        quick_sort(arr, center+1, right)

for t in range(int(input())):
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(*arr)