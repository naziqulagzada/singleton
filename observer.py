from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class State(ABC):
    @abstractmethod
    def status(self):
        pass

class Active(State):
    def status(self):
        return "The system is activated."

class Deactivate(State):
    def status(self):
        return "The system is deactivated."

class Sleep(State):
    def status(self):
        return  "The system is in sleep mode."

class SystemContext:
    def __init__(self):
        self._state = None
        self._observers = []

    def set_state(self, state: State):
        self._state = state
        self.notify_observers()

    def get_state(self):
        return self._state.status()

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def notify_observers(self):
        for obs in self._observers:
            obs.update(self._state)

class Logger(Observer):
    def update(self, state):
        print(f"[LOG] State changed -> {state.status()}")

if __name__ == "__main__":
    system = SystemContext()
    logger = Logger()

    system.attach(logger)

    system.set_state(Active())
    system.set_state(Sleep())
    system.set_state(Deactivate())



