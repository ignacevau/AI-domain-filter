import logging

from config import Config
from domain_filter.filter import DomainFilter
from registrar.providers.namecheap.provider import NamecheapProvider
from registrar.providers.provider import Provider


class Application:
    def __init__(self):
        self._output_file = None

        self.setup()

    def setup(self):
        # open the output file in append mode
        self._output_file = open(Config.OUTPUT_FILE, "a")

        logging.info("Application setup complete.")

    def run(self):
        # Main application logic
        logging.info("Application is running.")

        try:
            domain_filter = DomainFilter()
            providers: list[Provider] = []

            # add all providers
            providers.append(NamecheapProvider())

            # fetch and process data
            for provider in providers:
                while provider.has_next_page():
                    unfiltered_domains = provider.get_next_data()
                    filtered_domains = domain_filter.filter(unfiltered_domains)

                    for domain in filtered_domains:
                        self._output_file.write(f"{domain.as_csv()}\n")
        except KeyboardInterrupt:
            logging.warning("Application interrupted by user.")
        finally:
            self.cleanup()

    def cleanup(self):
        # Clean up resources before exiting
        if self._output_file:
            self._output_file.close()

        logging.info("Application cleanup complete.")
