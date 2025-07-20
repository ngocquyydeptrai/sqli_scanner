import time
from bs4 import BeautifulSoup
from .base_scanner import BaseScanner
from utils.request_handler import make_request
from utils.logger import logger

class BooleanBasedScanner(BaseScanner):
    def __init__(self, target, config):
        super().__init__(target, config)
        self.name = "Boolean-based SQLi Scanner"
        self.payloads = self.load_payloads('boolean_based')

    def test_payload(self, url, param, payload):
        try:
            test_url = self.build_test_url(url, param, payload)
            response = make_request(test_url, self.config)
            
            # Detection logic
            if self.detect_vulnerability(response):
                logger.warning(f"Vulnerable parameter: {param}")
                self.report_vulnerability(
                    type="Boolean-based SQLi",
                    parameter=param,
                    payload=payload,
                    evidence=response.text[:100] + "..."
                )
                return True
                
        except Exception as e:
            logger.error(f"Error testing {param}: {str(e)}")
        return False

    def detect_vulnerability(self, response):
        # Advanced detection logic
        error_patterns = [
            "SQL syntax",
            "unclosed quotation mark",
            "syntax error"
        ]
        return any(pattern in response.text.lower() for pattern in error_patterns)