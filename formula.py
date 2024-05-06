class MathFormula:

    # count the speed and time and return the distance
    def count_for_distance(self, speed, time, distance):
        if speed is None:
            return distance/time
        if time is None:
            return distance/speed
        if distance is None:
            return speed*time

math_formula = MathFormula()
# print(math_formula.count_for_distance(10, 20, None))
# print(math_formula.count_for_distance(10, None, 200))
print(math_formula.count_for_distance(None, 20, 200))