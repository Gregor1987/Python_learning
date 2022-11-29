class MinStat:
    def __init__(self, *args):
        self.numbers = list(map(int, args))

    def add_number(self, number):
        self.numbers.append(int(number))

    def result(self):
        if len(self.numbers) > 0:
            min_number = self.numbers[0]
            for i in range(1, len(self.numbers)):
                if self.numbers[i] < min_number:
                    min_number = self.numbers[i]
            return min_number
        else:
            return None


class MaxStat:
    def __init__(self, *args):
        self.numbers = list(map(int, args))

    def add_number(self, number):
        self.numbers.append(int(number))

    def result(self):
        if len(self.numbers) > 0:
            max_number = self.numbers[0]
            for i in range(1, len(self.numbers)):
                if self.numbers[i] > max_number:
                    max_number = self.numbers[i]
            return max_number
        else:
            return None


class AverageStat:
    def __init__(self, *args):
        self.numbers = list(map(int, args))

    def add_number(self, number):
        self.numbers.append(int(number))

    def result(self):
        if len(self.numbers) > 0:
            return sum(self.numbers) / len(self.numbers)
        else:
            return None


values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())

values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
