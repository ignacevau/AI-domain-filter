import logging
import sys

from app import Application


def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    # disable httpx logging
    logging.getLogger("httpx").setLevel(logging.WARNING)


def main():
    """Main entry point of the application"""
    setup_logging()
    # log that app started
    logging.info("Application started.")

    app = Application()
    app.run()


if __name__ == "__main__":
    main()
