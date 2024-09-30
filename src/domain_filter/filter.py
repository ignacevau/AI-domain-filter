import json
import logging

from config import Config
from domain_filter import ai_assistant
from registrar.domain import Domain


class DomainFilter:
    def __init__(self):
        self.assistant = ai_assistant.AIAssistant(Config.OPENAI_API_KEY)

    def filter(self, domains: list[Domain]) -> list[Domain]:
        domain_names = [domain.name for domain in domains]

        filtered_domain_names = self._get_filtered_domain_names(domain_names)
        logging.info(f"Filtered domain names: {filtered_domain_names}")

        # map the filtered domain names to the original domain objects
        filtered_domains = self._map_filtered_domains(domains, filtered_domain_names)

        return filtered_domains

    def _map_filtered_domains(
        self, domains: list[Domain], filtered_domain_names: list[str]
    ) -> list[Domain]:
        filtered_domains = []

        i, j = 0, 0

        # both lists are sorted, so we can iterate through them in linear time
        while i < len(domains) and j < len(filtered_domain_names):
            if domains[i].name == filtered_domain_names[j]:
                filtered_domains.append(domains[i])

                # move to the next filtered name since we've found a match
                j += 1
            # always move to the next original domain
            i += 1

        return filtered_domains

    def _get_filtered_domain_names(self, domain_names: list[str]) -> list[str]:
        retries = 0
        filtered_domains = []

        while retries <= Config.AI_PARSING_RETRIES:
            # get the filtered domains from the AI assistant
            unparsed_filtered_domains = self.assistant.get_domainfilter_response(
                domain_names
            )

            # parse the response into a list of domain names
            try:
                filtered_domains.extend(json.loads(unparsed_filtered_domains))
                break
            except json.JSONDecodeError:
                retries += 1
                if retries <= Config.AI_PARSING_RETRIES:
                    logging.error(
                        f"Error parsing AI response, retrying {retries}/{Config.AI_PARSING_RETRIES}."
                    )
                else:
                    logging.error(f"Error parsing AI response, max retries reached.")
                    return []

        return filtered_domains
