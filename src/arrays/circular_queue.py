class MovingAverage:
    def __init__(self, size: int):
        self.queue = [0] * size
        self.size = size
        self.window_sum = 0
        self.count = 0
        self.head = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.arr[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)
