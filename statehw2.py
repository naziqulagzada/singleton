from abc import ABC, abstractmethod

class TextState(ABC):
    @abstractmethod
    def change(self, text):
        pass

class SimpleState(TextState):
    def change(self, text):
        return f"The text in simple way is {text}."

class ReverseState(TextState):
    def change(self, text):
        return f"The text in reversed way is {''.join(reversed(text))}."

class Text:
    def __init__(self, text, state: TextState):
        self.text = text
        self.state = state

    def set_state(self, state: TextState):
        self.state = state

    def apply(self):
        return self.state.change(self.text)


if __name__ == "__main__":
    t1 = Text("Hello World!", SimpleState())
    print(t1.apply())

    t1.set_state(ReverseState())
    print(t1.apply())
