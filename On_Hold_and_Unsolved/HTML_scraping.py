'''
Issue: requests.exceptions.SSLError: HTTPSConnectionPool(host='www.nytimes.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)')))
'''

import requests, bs4

url_NYT = 'https://www.nytimes.com'

r = requests.get(url_NYT)

r_html = r.text

print(r_html)