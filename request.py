import json

BASE_URL = 'https://app.mintigo.com/api'
URL_SUFFIX = 'jwt-login'

PAYLOAD = {"password": "Anaplan21",
           "email": "mintigo20@gmail.com",
           "customerName": "Test24"}

HEADERS = "Content-Type"
HEADERS_TYPE = "application/json"


class Request:

    def __init__(self):

        self.config = None

        self.base_url = BASE_URL
        self.url_suffix = URL_SUFFIX
        self.url = None
        self.set_url()

        self.header_name = HEADERS
        self.header_type = HEADERS_TYPE
        self.headers = None
        self.set_headers()

        self.password = PAYLOAD['password']
        self.email = PAYLOAD['email']
        self.customerName = PAYLOAD['customerName']
        self.payload = None
        self.set_payload()

        self.set_config()

    def set_url(self,
                base_url=BASE_URL,
                url_suffix=URL_SUFFIX):
        self.url = f"{base_url}/{url_suffix}/"

        if self.config:
            self.set_config()

    def set_headers(self,
                    header_name=HEADERS,
                    header_type=HEADERS_TYPE):
        self.headers = {header_name: header_type}

        if self.config:
            self.set_config()

    def set_payload(self,
                    password=PAYLOAD['password'],
                    email=PAYLOAD['email'],
                    customerName=PAYLOAD['customerName']):
        self.payload = json.dumps({"password": password,
                                   "email": email,
                                   "customerName": customerName})

        if self.config:
            self.set_config()

    def set_config(self):

        self.config = {"url": self.url,
                       "headers": self.headers,
                       "data": self.payload}
