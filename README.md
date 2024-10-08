# Domain Filter Application

This is a Python-based application designed to filter domain names based on specific criteria using OpenAI's API. The program integrates with domain name providers like Namecheap to fetch domains, applies AI-powered filtering, and outputs the filtered domains to a CSV file.

The application will fetch and process ~300.000 domain names that are for sale on domain name auctions. The estimated cost for this using the `gpt-4o-mini`-model is 15 cents.

Currently only the Namecheap marketplace has been implemented, but the interface is set up to be easily expandable to other registrars.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

## Features

- **Domain Fetching**: Fetches domain data from Namecheap via their API.
- **AI-Powered Filtering**: Utilizes OpenAI's model to filter domain names based on predefined criteria.
- **Custom Configuration**: Modify filtering rules and provider settings through a `.env` file and `Config` class.
- **CSV Output**: Saves filtered domain names in a CSV format.
- **Scalable**: Supports additional domain providers with a clean, extensible provider interface.

## Installation

To run this application, make sure you have Python 3.11+ installed.

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/domain-filter.git
    cd domain-filter
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m virtualenv .venv
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the project root or copy the provided example file:

    ```bash
    cp .env.example .env
    ```

2. Fill in the required environment variables in the `.env` file:

    ```bash
    OPENAI_API_KEY=your_openai_api_key
    NAMECHEAP_API_KEY=your_namecheap_api_key
    ```

The application settings are defined in `src/config.py`:

- **BATCH_SIZE**: Number of domains to fetch in each batch.
- **PROCESSING_LIMIT**: Maximum number of domains to process.
- **DOMAIN_TLDS**: List of top-level domains (TLDs) to consider.
- **NO_HYPHENS** and **NO_NUMBERS**: Boolean flags to filter out domains with hyphens or numbers.
- **AI_PARSING_RETRIES**: Number of retries if the AI response fails to parse.
- **OUTPUT_FILE**: Path to the output CSV file.
- **SYSTEM_INTRO_PROMPT**: The system introduction prompt that OpenAI uses for the completion model. Current value should be acceptable for all cases.
- **SUCCESS_CONTEXT_PROMPT**: The prompt that explains the context for which the domain names are relevant. This is the only criteria that the OpenAI assistant will use to filter the domain names. Needs to be set to the user's desired context.
- **FORMATTING_PROMPT**: The prompt used to ensure proper formatting of the AI output. Current value should be acceptable for all cases.
- **OPENAI_MODEL**: The language model that OpenAI will use. Changing this is not recommended to prevent unexpected costs.


## Usage

1. Run the application:

    ```bash
    python src/main.py
    ```

2. The application will fetch domain data from Namecheap, apply AI-powered filtering, and store the results in a CSV file located at `./filtered_domains.csv`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.