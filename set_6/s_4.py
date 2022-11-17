N = 8
visited = [[0 for _ in range(N)] for _ in range(N)]
moves_counter=0
for row in visited:
    print(row)
print("------------------------------------")


def knights_tour_r(row=0, col=0):
    # def knights_tour_r(T: list[list], row=0, col=0):
    global visited
    global moves_counter
    if row in range(0, N) and col in range(0, N) and visited[row][col] == 0:
        visited[row][col] = 1
        moves_counter+=1
        # print(f"i={row} j={col}")
        # for table_row in visited:
        #     print(table_row)
        # print("------------------------------------")
        knights_tour_r(row - 2, col + 1)
        knights_tour_r(row - 1, col + 2)
        knights_tour_r(row + 1, col + 2)
        knights_tour_r(row + 2, col + 1)
        knights_tour_r(row + 2, col - 1)
        knights_tour_r(row + 1, col - 2)
        knights_tour_r(row - 1, col - 2)
        knights_tour_r(row - 2, col - 1)


knights_tour_r(0, 0)
print(moves_counter)