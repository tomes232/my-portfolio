"""Base state for the app."""

import reflex as rx


class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    show_spd_notebook: bool = False

    photo_index: int = 0
    photo_list: list[str] = ["prof.png", "1.png", "2.png", "3.png", "4.png"]
    photo: str = photo_list[photo_index]

    def answer(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know the answer to that question."
        self.chat_history.append((self.question, answer))


    def change_spd_notebook(self):
        self.show_spd_notebook = not self.show_spd_notebook

    def change_photo_back(self):
        self.photo_index = (self.photo_index - 1) % len(self.photo_list)
        self.photo = self.photo_list[self.photo_index]

    def change_photo_forward(self):
        self.photo_index = (self.photo_index + 1) % len(self.photo_list)
        self.photo = self.photo_list[self.photo_index]

 
    
    def get_photo(self) -> str:
        return self.photo_list[self.photo_index]

