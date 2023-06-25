import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temprature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a jock about birds")
    print(response)
