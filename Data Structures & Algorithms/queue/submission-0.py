class Deque:
    
    def __init__(self):
        self.eq = []

    def isEmpty(self) -> bool:
        return len(self.eq) == 0

    def append(self, value: int) -> None:
        self.eq.append(value)

    def appendleft(self, value: int) -> None:
        self.eq = [value] + self.eq

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        element = self.eq[-1]
        self.eq = self.eq[:-1]
        return element

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        element = self.eq[0]
        self.eq = self.eq[1:]
        return element
        
