import copy
import time


def cal_distance(source: tuple, destination: tuple) -> int:
    """ Cartesian distance between two points """
    return ((destination[0] - source[0]) ** 2 + (destination[1] - source[1]) ** 2) ** 0.5


def possible_move(maze: list[list], x: int, y: int) -> bool:
    if x >= len(maze[0]) or y >= len(maze) or x < 0 or y < 0 or maze[y][x] != 0:
        return False
    return True


def next_node(queue: dict) -> tuple:
    """ Returns the next element from the queue that has the lowest distance to destination. """
    current, min_distance = None, None

    for coord, val in queue.items():
        if current is None:
            current = coord
            min_distance = val

        if val < min_distance:
            current = coord
            min_distance = val

    return current


def astar(maze: list[list], start: tuple, finish: tuple) -> tuple[int, list[tuple]]:
    """
    A* search

    Parameters:
    - maze: The 2D matrix that represents the maze with 0 represents empty space and 1 represents a wall
    - start: A tuple with the coordinates of starting position
    - finish: A tuple with the coordinates of finishing position

    Returns:
    - Number of steps from start to finish, equals -1 if the path is not found
    - Viz - everything required for step-by-step vizualization
    
    """
    path = []
    if not possible_move(maze, x=start[1], y=start[0]) or not possible_move(maze, x=finish[1], y=finish[0]):
        return -1, path

    if start == finish:
        path.append(start)
        return len(path) - 1, path
    pri_queue = {start: cal_distance(start, finish)}

    while len(pri_queue) > 0:
        current = next_node(pri_queue)
        path.append(current)
        pri_queue.pop(current)

        c_x = current[1]
        c_y = current[0]

        neighbors = [(c_y, c_x + 1), (c_y, c_x - 1), (c_y + 1, c_x), (c_y - 1, c_x)]
        for neighbor in neighbors:
            if possible_move(maze, x=neighbor[1], y=neighbor[0]) and neighbor not in pri_queue and neighbor not in path:
                if neighbor == finish:
                    path.append(neighbor)
                    return len(path) - 1, path
                pri_queue[neighbor] = cal_distance(neighbor, finish)

    return -1, path


def print_maze(maze: list[list]) -> None:
    for row in maze:
        viz_row = '['
        for cell in row:
            viz_row += '\t' + str(cell)
        viz_row += '\t]'
        print(viz_row)


def vizualize(viz: list[tuple[int, int]], maze: list[list], num_steps: int) -> None:
    """
    Vizualization function. Shows step by step the work of the search algorithm

    Parameters:
    - viz: everything required for step-by-step vizualization
    """
    for i in range(len(viz)):
        node = viz[i]
        if i == 0:
            maze[node[0]][node[1]] = 'S'
        elif i == len(viz) - 1 and num_steps != -1:
            maze[node[0]][node[1]] = 'F'
        else:
            maze[node[0]][node[1]] = '.'
        print(f'\nStep {i}:')
        print_maze(maze)
        time.sleep(1)
    print("END")


# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

maze2 = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]


def manual_test(maze: list[list]):
    cont = 'y'
    while cont == 'y':
        print("\n\nEnter coordinates separated by comma (e.g. 2,3)")
        start = input("Enter the starting position:").split(',')
        try:
            start = (int(start[0]), int(start[1]))
        except Exception:
            print(f"\nError entering starting coordinates: {start} is not possible to convert to tuple[int, int], "
                  "please enter again the coordinates.")
            continue

        finish = input("Enter the finishing position:").split(',')
        try:
            finish = (int(finish[0]), int(finish[1]))
        except Exception:
            print(f"\nError entering finishing coordinates: {finish} it is not possible to convert to tuple[int, int], "
                  "please enter again the coordinates.")
            continue

        num_steps, viz = astar(maze, start, finish)

        # Print number of steps in path
        if num_steps != -1:
            print(f"Path from {start} to {finish} using A* is {num_steps} steps.")
        else:
            print(f"No path from {start} to {finish} exists.")

        copy_maze = copy.deepcopy(maze)
        vizualize(viz, copy_maze, num_steps)
        cont = input("\n\nContinue with manual tests? (y/n): ")


def test_case(num: int,maze: list[list], start_position: tuple, finish_position: tuple):
    print("------------------------------------------------------------------------")
    print(f"Test {num}:")
    print(f'Starting position: {start_position}, finish position: {finish_position}')

    num_steps, viz = astar(maze, start_position, finish_position)

    # Print number of steps in path
    if num_steps != -1:
        print(f"Path from {start_position} to {finish_position} using A* is {num_steps} steps.")
    else:
        print(f"No path from {start_position} to {finish_position} exists.")

    # Vizualize algorithm step-by-step even if the path was not found
    copy_maze = copy.deepcopy(maze)
    vizualize(viz, copy_maze, num_steps)


def test_cases(maze: list[list]):
    print("\n\nTest cases:")

    # Edge to edge of the map and vice-versa.
    test_case(1, maze, (0, 0), (4, 4))
    test_case(2, maze, (0, 0), (4, 0))
    test_case(3, maze, (0, 0), (0, 4))

    test_case(4, maze, (0, 4), (0, 0))
    test_case(5, maze, (0, 4), (4, 4))
    test_case(6, maze, (0, 4), (4, 0))

    test_case(7, maze, (4, 0), (0, 0))
    test_case(8, maze, (4, 0), (0, 4))
    test_case(9, maze, (4, 0), (4, 4))

    test_case(10, maze, (4, 4), (0, 0))
    test_case(11, maze, (4, 4), (0, 4))
    test_case(12, maze, (4, 4), (4, 0))

    # Same starting point and ending point.
    test_case(13, maze, (4, 4), (4, 4))

    # Invalid position.
    test_case(14, maze, (5, 5), (4, 0))
    test_case(15, maze, (0, 1), (4, 4))
    test_case(16, maze, (0, 0), (3, 2))
    test_case(17, maze, (0, 0), (5, 4))

    print("------------------------------------------------------------------------")
    print("END TEST CASES")


if __name__ == '__main__':
    print("Lab 1 EARIN: A* algorithm implementation by Krzysztof Kotowski and Juan Manuel Aristizabal Henao.")
    sel = int(input("If you want to run manually the test cases input 1, "
                    "\nelse if you want to run the test cases input 0. "
                    "\nInput: "))
    if sel == 0:
        test_cases(maze)
    elif sel == 1:
        manual_test(maze)
