from abc import ABC, abstractmethod


class ElevatorState(ABC):
    @abstractmethod
    def button(self, floor):
        pass


class UpState(ElevatorState):
    def button(self, floor):
        return f"The elevator is going up to {floor}th floor."

class DownState(ElevatorState):
    def button(self, floor):
        return f"The elevator is going down to {floor}th floor."


class Elevator:
    def __init__(self, floor, state: ElevatorState):
        self.floor = floor
        self.state = state

    def set_state(self, state: ElevatorState):
        self.state = state

    def press_button(self):
        return self.state.button(self.floor)


if __name__ == "__main__":
    elevator = Elevator(2, UpState())
    print(elevator.press_button())

    elevator.set_state(DownState())
    print(elevator.press_button())
