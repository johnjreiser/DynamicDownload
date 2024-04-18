import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from retrying import retry
from time import sleep
import pickle

logging.basicConfig(level=logging.INFO)


class HeadlessBrowser(object):
    def __init__(self):
        # mobile_emulation = {"deviceName": "Nexus 5"}
        opts = webdriver.ChromeOptions()
        # opts.add_argument("--window-size=393,851")
        opts.add_argument("--disable-extensions")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--no-sandbox")
        # opts.add_argument("--auto-open-devtools-for-tabs")
        # opts.add_argument("--use-mobile-user-agent")
        # opts.add_experimental_option("mobileEmulation", mobile_emulation)

        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub", options=opts
        )
        self.cookies = {}

    def get_urls(self, site, fileExts=None):
        urls = []
        try:
            logging.info(f"Requesting {site}...")
            self.driver.get(site)
            logging.info("Downloaded.")
            sleep(2)
            if not fileExts:
                return self.driver
            else:
                if isinstance(fileExts, str):
                    fileExts = [fileExts]
                tags = self.driver.find_elements(By.TAG_NAME, "a")
                for tag in tags:
                    href = tag.get_attribute("href")
                    for ext in fileExts:
                        if ext in href:
                            urls.append(href)
        except Exception as e:
            logging.error(e)
        return urls

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL of page to fetch")
    parser.add_argument(
        "-x",
        "--extension",
        help="Extension(s) to search for within A HREF attributes.",
        nargs="*",
    )
    args = parser.parse_args()

    try:
        hb = HeadlessBrowser()
        [print(x) for x in hb.get_urls(args.url, args.extension)]
    except Exception as e:
        logging.error(e)
    finally:
        hb.close()
        hb.quit()
