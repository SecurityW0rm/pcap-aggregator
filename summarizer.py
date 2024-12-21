import openai

def generate_summary(logs, api_key):
    openai.api_key = api_key

    # Prepare logs as a string for the AI to process
    logs_text = "\n".join([f"{key}: {count}" for key, count in logs.items()])
    prompt = f"Here are some aggregated logs:\n{logs_text}\n\nProvide a concise summary of the logs and highlight any unusual activity."

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        raise Exception(f"Error generating summary: {e}")
