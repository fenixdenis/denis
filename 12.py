class Things:
    pass


class Inanimaite(Things):
    pass


class Animate(Things):
    pass


class Sidewalks(Inanimaite):
    pass


class Animals(Animate):
    pass


class Mammals(Animals):
    pass


class Giraffes(Mammals):
    def left_foot_forward(self):
        print('Left foot forward')
    def right_foot_back(self):
        print('Right foot back')


reginald = Giraffes()
for i in range(10):
    reginald.left_foot_forward()
    reginald.right_foot_back()
