from g4f.client import Client

def main():
    client = Client()

    try:
        # Create a chat completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
        )

        # Print the response from the model
        print("Assistant:", response.choices[0].message.content)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
