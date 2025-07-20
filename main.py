import argparse
from scanners.boolean_based import BooleanBasedScanner
from scanners.time_based import TimeBasedScanner
from utils.logger import setup_logger
from utils.config import load_config

logger = setup_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description='SQL Injection Scanner')
    parser.add_argument('-u', '--url', required=True, help='Target URL')
    parser.add_argument('--level', type=int, default=3, 
                      help='Scan level (1-5, higher=more thorough)')
    parser.add_argument('--proxy', help='Proxy server (e.g. http://127.0.0.1:8080)')
    parser.add_argument('--output', help='Output file (JSON/HTML)')
    args = parser.parse_args()

    config = load_config()
    
    logger.info(f"Starting scan on {args.url}")
    
    # Run scanners
    scanners = [
        BooleanBasedScanner(args.url, config),
        TimeBasedScanner(args.url, config)
    ]
    
    for scanner in scanners:
        scanner.run(level=args.level)
    
    logger.info("Scan completed")

if __name__ == '__main__':
    main()