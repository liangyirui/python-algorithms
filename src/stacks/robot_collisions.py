"""
There are n 1-indexed robots, each having a position on a line, health, and movement direction.
You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.
All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.
If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.
Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.
Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.
Note: The positions may be unsorted.
"""


def survived_robots_healths(
    positions: list[int], healths: list[int], directions: str
) -> list[int]:
    n = len(positions)
    indices = list(range(n))
    indices.sort(key=lambda x: positions[x])
    stack = []
    survived = []
    for curr_id in indices:
        if directions[curr_id] == "R":
            stack.append(curr_id)
            continue
        while stack and healths[curr_id] > 0:
            top_id = stack.pop()
            if healths[top_id] < healths[curr_id]:
                healths[top_id] = 0
                healths[curr_id] -= 1
            elif healths[top_id] > healths[curr_id]:
                healths[top_id] -= 1
                healths[curr_id] = 0
                stack.append(top_id)
            else:
                healths[top_id] = 0
                healths[curr_id] = 0

    for i in range(n):
        if healths[i] > 0:
            survived.append(healths[i])
    return survived


if __name__ == "__main__":
    positions = [3, 5, 2, 6]
    healths = [10, 10, 15, 12]
    directions = "RLRL"
    print(survived_robots_healths(positions, healths, directions))
