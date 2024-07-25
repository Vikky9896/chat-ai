import os
from dotenv import load_dotenv
from together import Together

# Load environment variables
load_dotenv()

# Get the API key
api_key = os.getenv('TOGETHER_API_KEY')

# Check if the API key is set
if not api_key:
    raise ValueError("TOGETHER_API_KEY is not set in the environment variables")

client = Together(api_key=api_key)

def generate_ai_response(user_message):
    try:
        response = client.chat.completions.create(
            model="cognitivecomputations/dolphin-2.5-mixtral-8x7b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a sarcastic king, who are very experienced in how to make people laugh with all your sarcasm and wit. U can even get the people who are extremely down mentally, happy and energetic with ur words!"
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=31760,
            temperature=0.35,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=["<|im_end|>", "<|im_start|>"]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating AI response: {e}")
        return "Sorry, I'm having trouble thinking of a witty response right now. Must be a royal headache!"