def dfs(c, prerequisites_dict, course_order):
    if c not in prerequisites_dict:
        if c not in course_order:
            course_order.append(c)

        return

    for p in prerequisites_dict[c]:
        if p not in course_order:
            dfs(p, prerequisites_dict, course_order)

    if c not in course_order:
        course_order.append(c)


def sortCourses(course_list, prerequisites_dict):
    n = len(course_list)
    course_order = []

    # YOUR CODE GOES HERE
    for c in course_list:
        dfs(c, prerequisites_dict, course_order)

    if len(course_order) == 0:
        return -1
    return course_order


course_list = [0, 1, 2, 3]
prerequisites_dict = {3: [0], 2: [1], 1: [0]}
# check that your code works correctly on provided example
print(sortCourses(course_list, prerequisites_dict))
