import heapq
import math

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def heuristic(a, b):
    return math.hypot(b[0] - a[0], b[1] - a[1]) 

def a_star(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_set = [(0 + heuristic(start, end), 0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, curr_g, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (1, 1), (-1, 1), (1, -1)]:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if not is_valid(nx, ny, rows, cols) or grid[nx][ny] == 0:
                continue

            tentative_g = curr_g + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, end)
                heapq.heappush(open_set, (f, tentative_g, neighbor))
                came_from[neighbor] = current

    return None

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter the grid (0 = blocked, 1 = unblocked):")
    grid = [list(map(int, input().split())) for _ in range(rows)]

    sx, sy = map(int, input("Enter source (row col): ").split())
    ex, ey = map(int, input("Enter destination (row col): ").split())
    start, end = (sx, sy), (ex, ey)

    if not is_valid(sx, sy, rows, cols) or not is_valid(ex, ey, rows, cols) or grid[sx][sy] == 0 or grid[ex][ey] == 0:
        print("Invalid source or destination.")
        return

    path = a_star(grid, start, end)
    if path:
        print("Path found:")
        for step in path:
            print("->", step, end=" ")
        print()
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
