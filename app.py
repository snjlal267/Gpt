from g4f.client import Client

def main():
    client = Client()

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit the loop if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break

        try:
            # Create a chat completion using user input
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": user_input}],
            )
            
            # Print the response from the model
            print("Assistant:", response.choices[0].message.content)

        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
