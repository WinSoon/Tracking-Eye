import numpy as np

class GridSplitterAlgorithm(object):
    def __init__(self, width, height, grid_size, histeresis):
        # Note, if histeresis is 0, then it is disabled
        assert(histeresis >= 0 and histeresis <= 1.0)
        self.width = width
        self.height = height
        self.amount_of_rows = grid_size[0]
        self.amount_of_cols = grid_size[1]

        assert(self.amount_of_cols > 0 and self.amount_of_rows > 0)

        self.step_rows = self.height / float(self.amount_of_rows)
        self.step_cols = self.width / float(self.amount_of_cols)
        self.histeresis = histeresis

        assert(self.step_rows != 0 and self.step_cols != 0)

    def find_grid_position(self, object_x, object_y):
        # NOTE: Object x corresponds to columns and object_y to rows
        assert(object_x >= 0 and object_x < self.width)
        assert(object_y >= 0 and object_y < self.height)

        grid_col = int(object_x / self.step_cols)
        grid_row = int(object_y / self.step_rows)
        return [grid_row, grid_col]

    def check_change(self, object_x, object_y, old_grid, new_grid):
        # NOTE: Object x corresponds to columns and object_y to rows
        diff = np.array(new_grid) - np.array(old_grid)
        ret_rows = False
        ret_cols = False

        if np.any(diff):
            # There might be a change
            rows_diff = new_grid[0] - old_grid[0]
            if rows_diff:
                # if diff > 0 --> move down
                ret_rows = self.is_out_histeresis(
                    object_y,
                    self.step_rows,
                    self.histeresis,
                    old_grid[0],
                    rows_diff
                )

            cols_diff = new_grid[1] - old_grid[1]
            if cols_diff:
                # if diff > 0 --> move right
                ret_cols = self.is_out_histeresis(
                    object_x,
                    self.step_cols,
                    self.histeresis,
                    old_grid[1],
                    cols_diff
                )

        # If any, rows or colums change, an update is required
        return ret_cols or ret_rows

    def is_out_histeresis(self, obj_pos, step, histeresis, old_grid_val, diff):
        grid_cell = obj_pos / step
        if diff > 0:
            if int(grid_cell - histeresis) - old_grid_val:
                return True
        else:
            if int(grid_cell + histeresis) - old_grid_val:
                return True

        return False

if __name__ == '__main__':
    obj = GridSplitterAlgorithm(640, 480, [3, 3], 0.1)

    print("------ Initialization test ----------")
    old_grid = [-1, -1]
    object_x = 100
    object_y = 400
    grid_pos = obj.find_grid_position(object_x, object_y)
    print("Old grid: {}".format(old_grid))
    print("new grid: {}".format(grid_pos))
    ret = obj.check_change(object_x,object_y, old_grid, grid_pos)
    print("Change needed? {}".format("True" if ret else "False"))

    print("------ No update test ----------")
    old_grid = [2,1]
    object_x = 300
    object_y = 400
    grid_pos = obj.find_grid_position(object_x, object_y)
    print("Old grid: {}".format(old_grid))
    print("new grid: {}".format(grid_pos))
    ret = obj.check_change(object_x, object_y, old_grid, grid_pos)
    print("Change needed? {}".format("True" if ret else "False"))

    print("------ Histeresis test ----------")
    old_grid = [2,1]
    object_x = 190
    object_y = 400
    grid_pos = obj.find_grid_position(object_x, object_y)
    print("Old grid: {}".format(old_grid))
    print("new grid: {}".format(grid_pos))
    ret = obj.check_change(object_x, object_y, old_grid, grid_pos)
    print("Change needed? {}".format("True" if ret else "False"))