'''
    이 문제의 경우 binary search를 연습하기 위해 일부러 binary search를 구현하는 방식으로 갔지만,
    문제 구성상 target in total_list로 찾으면 한번에 해결되긴 한다.
'''
def main():

    with open('input.txt', 'r') as fp:
        lines = fp.readlines()
    lines = [ line.strip() for line in lines ]

    total_num = int(lines[0])
    assert 1 <= total_num <= 1e6

    total_list = list(map(int, lines[1].split(' ')))
    assert len(total_list) == total_num and len([x for x in total_list if not (1 <= x <= 1e6)]) == 0

    num_targets = int(lines[2])
    assert 1 <= num_targets <= 1e5

    targets = list(map(int, lines[3].split(' ')))
    assert len(targets) == num_targets and len([x for x in targets if not (1 <= x <= 1e6)]) == 0

    total_list.sort()
    for target in targets:
        result = binary_search(target, total_list, 0, total_num - 1)
        if result is not None:
            print('yes', end=' ')
        else:
            print('no', end=' ')
    print('\n')

    return

def binary_search(target, given_list, start, end):

    #   # 반복문을 이용한 풀이
    #   while start <= end:
    #       mid = (start + end) // 2

    #       if given_list[mid] == target:
    #           return mid
    #       elif given_list[mid] > target:
    #           end = mid - 1
    #       else:
    #           start = mid + 1

    #   return None

    # 재귀함수를 이용한 풀이
    if start > end:
        return None
    
    mid = (start + end) // 2
    if given_list[mid] == target:
        return mid
    else:
        if given_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return binary_search(target, given_list, start, end)


if __name__ == '__main__':
    main()