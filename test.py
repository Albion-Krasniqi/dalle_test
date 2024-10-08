import openai
import dotenv
import os


dotenv.load_dotenv()

# Set up the OpenAI client with the API key from the environment
client = openai.OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)
