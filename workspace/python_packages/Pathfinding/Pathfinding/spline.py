from Pathfinding import Position


class QuinitcSpline:
    """Class that represents one quintic spline which consists of a quintic polynomial for each dimension (x and y)."""

    def __init__(self, all_positions, position_index):

        # fill input-vector with information not depending on whether all_positions[position_index-1] and all_positions[position_index+2] exist

        if position_index > 0:  # if there is 1 previous position
            # fill input-vector accordingly
            pass
        elif position_index == 0:  # if there is no previous position
            #  fill input-vector accordingly
            pass

        if (
            position_index < len(all_positions) - 2
        ):  # if there are 2 following positions
            # fill input-vector accordingly
            pass
        elif (
            position_index < len(all_positions) - 1
        ):  # if there is only one following position
            # fill input-vector accordingly
            pass

        # do inverse-matrix multiplication -> maybe inside Polygon-class???
        # https://numpy.org/doc/stable/reference/generated/numpy.matmul.html (Matrix-Multiplikation)
        # https://numpy.org/doc/stable/reference/generated/numpy.matrix.transpose.html (Matrix-Transposition)
