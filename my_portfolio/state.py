"""Base state for the app."""

import reflex as rx

from typing import List

import requests

import pprint



models: List[str] = ["distilbert", "openai"]

photo_list: List[str] = ["prof.png", "1.png", "2.png", "3.png", "4.png"]




class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    show_spd_notebook: bool = False

    photo_index: int = 0
    photo: str = photo_list[photo_index]

    model: str = "openai"

    thread: str = None

    def answer(self):
        # Our chatbot is not very smart right now...

        if self.question == "":
            answer = "Please ask a question."
        if self.model == "models":
            answer = "Please select a model."
        elif self.model == "distilbert":
            input = {"input": self.question}
            # make a post api call to http://164.90.140.91/model/{model} with input
            response = requests.put("http://164.90.140.91/model/" + self.model, json=input)
            answer = response.json()["output"]
        elif self.model == "openai":
            print(self.thread)
            print(self.question)
            if self.thread:
                input = {"input": self.question, "session_id": self.thread}
            else:
                input = {"input": self.question}

            pprint.pprint(input)
            # make a post api call to http://164.90.140.91/model/{model} with input
            response = requests.put("http://164.90.140.91/model/" + self.model, json=input)

            pprint.pprint(response.json())

            if not response.json().get("output"):
                answer = "Sorry, I don't know the answer to that question."
            else:
                answer = response.json()["output"]
                self.thread = response.json()["session_id"]


        self.chat_history.append((self.question, answer))
        self.question = ""


    def change_spd_notebook(self):
        self.show_spd_notebook = not self.show_spd_notebook

    def change_photo_back(self):
        self.photo_index = (self.photo_index - 1) % len(photo_list)
        self.photo = photo_list[self.photo_index]

    def change_photo_forward(self):
        self.photo_index = (self.photo_index + 1) % len(photo_list)
        self.photo = photo_list[self.photo_index]

 
    
    def get_photo(self) -> str:
        return self.photo_list[self.photo_index]

    def set_option(self, option: str):
        self.model = option



