import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Config:
    # Non-sensitive app configuration
    BATCH_SIZE: int = 100
    PROCESSING_LIMIT: int | None = 200
    DOMAIN_TLDS: list[str] = ["com", "ai", "energy", "solar"]
    NO_HYPHENS: bool = True
    NO_NUMBERS: bool = True

    SYSTEM_INTRO_PROMPT: str = (
        """You are a processing bot that receives a list of domain names and filters those domain names by whether they would be a good fit for the following description:"""
    )
    SUCCESS_CONTEXT_PROMPT: str = (
        """An energy platform that allows users to monitor, manage and optimize their energy usage in their household. It integrates with solar panels, electric vehicles, home batteries, smart plugs, inverters, etc. Some of the most important features include: viewing history of a variety of measures, controlling the home devices and vehicles as well as the inverter, and optimizing, planning and automating energy usage in the future. There is a focus on AI for future predictions."""
    )
    FORMATTING_PROMPT: str = (
        """You return all the domain names that are a good fit for this description. Your output format is a single array with the domain names as strings in valid JSON. Your output must not be in Markdown, but be parseable JSON."""
    )

    OPENAI_MODEL: str = "gpt-4o-mini"
    # Number of times to retry parsing the AI response in case of failure
    AI_PARSING_RETRIES: int = 3

    OUTPUT_FILE: str = "./filtered_domains.csv"

    # Environment variables (sensitive or environment-specific)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    NAMECHEAP_API_KEY = os.getenv("NAMECHEAP_API_KEY")
