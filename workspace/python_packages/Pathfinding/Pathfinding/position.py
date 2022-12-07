class Position:
    """Class that represents a position which is basically a tuple of an x-, y- and phi- (orientation) value."""

    def __init__(self, x, y, phi, angle_mutable):
        self.x = x
        self.y = y
        self.phi = phi
        self.angle_mutable = angle_mutable
