import requests
from urllib3.exceptions import InsecureRequestWarning
from .logger import logger

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def make_request(url, config, method='GET', data=None):
    headers = {
        'User-Agent': config['user_agent'],
        'Accept': 'text/html,application/xhtml+xml'
    }
    
    try:
        if method.upper() == 'GET':
            response = requests.get(
                url,
                headers=headers,
                verify=False,
                timeout=config['timeout'],
                proxies=config.get('proxy')
            )
        else:
            response = requests.post(
                url,
                headers=headers,
                data=data,
                verify=False,
                timeout=config['timeout'],
                proxies=config.get('proxy')
            )
            
        return response
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None