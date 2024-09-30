import datetime as dt
import logging

import requests

from config import Config
from registrar.domain import Domain
from registrar.providers.provider import Provider

from .constants import MARKETPLACE_SALES_URL


class NamecheapProvider(Provider):
    def _fetch_data(self, chunk_page: int) -> list[dict]:
        try:
            params = {
                "noHyphens": "true" if Config.NO_HYPHENS else "false",
                "noNumbers": "true" if Config.NO_NUMBERS else "false",
                "tld": ",".join(Config.DOMAIN_TLDS),
                "pageSize": Config.BATCH_SIZE,
                "page": chunk_page,
            }
            headers = {"Authorization": f"Bearer {Config.NAMECHEAP_API_KEY}"}

            response = requests.get(
                MARKETPLACE_SALES_URL,
                params=params,
                headers=headers,
            )
            data = response.json()

            # update the chunk information
            self._current_chunk = chunk_page
            self._total_chunks = data["pages"]["lastPage"]

            logging.info(f"Fetching page {self._current_chunk}/{self._total_chunks}")

            return data["items"]
        except Exception as e:
            logging.error(f"Error fetching data from Namecheap: {e}")
            return []

    def _parse_data(self, data: list[dict]) -> list[Domain]:
        domains = []
        for item in data:
            try:
                domains.append(
                    Domain(
                        name=item["name"],
                        price=item["price"],
                        min_bid=item["minBid"],
                        expiration=dt.datetime.fromisoformat(item["endDate"]),
                        renew_price=item["renewPrice"],
                        bid_count=item["bidCount"],
                    )
                )
            except Exception as e:
                logging.error(f"Error processing domain {item['name']}: {e}")

        return domains  # Return the processed data
