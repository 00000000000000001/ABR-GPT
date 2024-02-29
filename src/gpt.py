from openai import OpenAI
import config

client = OpenAI(
    api_key=config.API_KEY,
)

def abr_gpt(string):
    completion = client.chat.completions.create(
        model=config.GPT_MODEL,
        messages=[
            {
                "role": "system",
                "content": config.PROMPT,
            },
            {"role": "user", "content": string},
        ],
    )

    return completion.choices[0].message.content
