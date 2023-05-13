import openai

class ChatGpt:

    def getMessage(self, question):
        openai.api_key_path = ".openAiKey"

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=2000,
            messages=[
                {"role": "user", "content": question}]
        )

        response = completion.choices[0].message.content
        return response
