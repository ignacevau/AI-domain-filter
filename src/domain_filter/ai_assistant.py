from openai import OpenAI

from config import Config


class AIAssistant:
    def __init__(self, api_key):
        self.api_key = api_key

        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY,
        )

    def get_domainfilter_response(self, domains: list[str]) -> str:
        response = self.client.chat.completions.create(
            model=Config.OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": f"""{Config.SYSTEM_INTRO_PROMPT}\n\"{Config.SUCCESS_CONTEXT_PROMPT}\"\n\n{Config.FORMATTING_PROMPT}""",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "\n".join(domains),
                        }
                    ],
                },
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={"type": "text"},
        )

        # get the response message
        unparsed_list = response.choices[0].message.content

        return unparsed_list
