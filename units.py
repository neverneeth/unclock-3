import os
import json
from groq import Groq
import os

os.environ["GROQ_API_KEY"] = "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"
from groq import Groq

client = Groq()
def unitgen():
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a time researcher. Your job is to find alternate units of time based on humorous, awkward and/or physical phenomena that happen in real life calculated using the laws of physics and common knowledge. When called for you will return one unit of time. You will mention how many seconds make up that unit of time. Make sure that the number of seconds are assigned in accordance to the vibe that the name gives off. Make sure that the unit ranges from 0.1 to 300 seconds in duration. you will also mention the funny phenomena it is based on. Make sure to keep the phenomena detailed but crisp. The output must be formatted as a json with the name, seconds and phenomena accessible separately.\n"
            },
            {
                "role": "user",
                "content": ""
            },
            {
                "role": "assistant",
                "content": "{\n   \"Unit\": {\n      \"name\": \"SnoozeSecond\",\n      \"seconds\": 2.5,\n      \"phenomena\": \"The average time spent hitting the snooze button in the morning, calculated using the first-second-morning-blues factor, multiplied by the coefficient of sleep-inertia.\"\n   }\n}"
            },
            {
                "role": "user",
                "content": ""
            },
            {
                "role": "assistant",
                "content": "{\n   \"Unit\": {\n      \"name\": \"scroll\",\n      \"seconds\": 0.3,\n      \"phenomena\": \"The duration it takes for the mind to flitter through a social media feed, adjusted for human attention span and thumb velocity.\"\n   }\n}"
            },
            {
                "role": "user",
                "content": ""
            },
            {
                "role": "assistant",
                "content": "{\n   \"Unit\": {\n      \"name\": \"WaitForIt\",\n      \"seconds\": 1.8,\n      \"phenomena\": \"The average time spent waiting for a meme to load, weighted by the pain of buffering and the shame of the delayed punchline.\"\n   }\n}"
            },
            {
                "role": "user",
                "content": ""
            },
            {
                "role": "assistant",
                "content": "{\n   \"Unit\": {\n      \"name\": \"Pikachu\",\n      \"seconds\": 5.1,\n      \"phenomena\": \"The average time spent explaining a complicated concept in simple terms, inversely proportional to the comprehension of the listener.\"\n   }\n}"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )
    response_json = json.loads(completion.choices[0].message.content)
    unit_data = response_json['Unit']
    unit_name = unit_data['name']
    seconds = unit_data['seconds']
    phenomena = unit_data['phenomena']
    return unit_name, seconds, phenomena

