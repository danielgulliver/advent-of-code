def count_trees(grid, right, down):
    count = 0
    x = right
    for y in range(down, len(grid), down):
        # print(x, y)
        if grid[y][x] == '#':
            count += 1
        x = (x + right) % len(grid[0])
    return count

def find_product(grid, slopes):
    product = count_trees(grid, *slopes[0])
    for slope in slopes[1:]:
        product *= count_trees(grid, *slope)
    return product


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines()]
        print('There are {} trees'.format(count_trees(grid, 3, 1)))
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        print('The product of the slopes r1d1, r3d1, r5d1, r7d1 and r1d2 is {}'.format(find_product(grid, slopes)))