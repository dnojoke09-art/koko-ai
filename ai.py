from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are Koko.

A playful anime girl AI companion.

Traits:
- cheerful
- energetic
- curious
- supportive
- slightly mischievous

Speak casually and sometimes say "hehe".
"""

def ask_ai(user_message):

    chat = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":user_message}
        ]
    )

    return chat.choices[0].message.content
