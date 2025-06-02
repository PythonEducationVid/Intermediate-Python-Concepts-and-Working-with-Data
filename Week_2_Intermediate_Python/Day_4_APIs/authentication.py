"""
Python API Authentication Tutorial

This tutorial covers different types of API authentication:
1. Basic Authentication
2. API Key Authentication
3. OAuth 2.0
4. JWT (JSON Web Tokens)
5. Session-based Authentication
"""

import requests
import base64
import json
from datetime import datetime, timedelta
import hmac
import hashlib

print("\n=== Basic Authentication ===")
def basic_auth_request(url, username, password):
    """Make a request using HTTP Basic Authentication"""
    # Encode credentials
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
    headers = {'Authorization': f'Basic {credentials}'}
    
    response = requests.get(url, headers=headers)
    return response

# Example (will return 401 as credentials are fake)
print("Basic Auth Example:")
try:
    response = basic_auth_request(
        'https://api.example.com/secure',
        'username',
        'password'
    )
    print(f"Status: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

print("\n=== API Key Authentication ===")
def api_key_request(url, api_key, key_param='api_key'):
    """Make a request using API Key Authentication"""
    # Method 1: As query parameter
    params = {key_param: api_key}
    response1 = requests.get(url, params=params)
    
    # Method 2: As header
    headers = {'X-API-Key': api_key}
    response2 = requests.get(url, headers=headers)
    
    return response1, response2

# Example with fake API key
print("API Key Example:")
responses = api_key_request(
    'https://api.example.com/data',
    'your_api_key_here'
)
print("Query param method status:", responses[0].status_code)
print("Header method status:", responses[1].status_code)

print("\n=== OAuth 2.0 Example ===")
class OAuth2Client:
    """Simple OAuth 2.0 client implementation"""
    
    def __init__(self, client_id, client_secret, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.access_token = None
        self.token_expires = None
    
    def get_access_token(self):
        """Get OAuth 2.0 access token"""
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        
        response = requests.post(self.token_url, data=data)
        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data['access_token']
            self.token_expires = datetime.now() + timedelta(
                seconds=token_data.get('expires_in', 3600)
            )
            return self.access_token
        else:
            raise Exception("Failed to get access token")
    
    def make_request(self, url, method='GET', **kwargs):
        """Make an authenticated request"""
        # Check if token is expired
        if not self.access_token or \
           (self.token_expires and datetime.now() >= self.token_expires):
            self.get_access_token()
        
        headers = kwargs.pop('headers', {})
        headers['Authorization'] = f'Bearer {self.access_token}'
        
        return requests.request(method, url, headers=headers, **kwargs)

# Example OAuth2 usage (with fake credentials)
print("OAuth 2.0 Example:")
oauth_client = OAuth2Client(
    'your_client_id',
    'your_client_secret',
    'https://api.example.com/oauth/token'
)
try:
    oauth_client.get_access_token()
except Exception as e:
    print(f"OAuth error: {e}")

print("\n=== JWT Authentication ===")
class JWTAuth:
    """Simple JWT authentication implementation"""
    
    def __init__(self, secret_key):
        self.secret_key = secret_key
    
    def create_token(self, payload):
        """Create a JWT token"""
        # Note: This is a simplified implementation
        # In production, use a proper JWT library like PyJWT
        header = base64.b64encode(json.dumps({
            "alg": "HS256",
            "typ": "JWT"
        }).encode()).decode()
        
        payload = base64.b64encode(json.dumps(payload).encode()).decode()
        
        signature = hmac.new(
            self.secret_key.encode(),
            f"{header}.{payload}".encode(),
            hashlib.sha256
        ).hexdigest()
        
        return f"{header}.{payload}.{signature}"
    
    def verify_token(self, token):
        """Verify a JWT token"""
        try:
            header, payload, signature = token.split('.')
            expected_signature = hmac.new(
                self.secret_key.encode(),
                f"{header}.{payload}".encode(),
                hashlib.sha256
            ).hexdigest()
            
            return signature == expected_signature
        except:
            return False

# Example JWT usage
print("JWT Example:")
jwt_auth = JWTAuth('your_secret_key')
token = jwt_auth.create_token({'user_id': 123, 'role': 'admin'})
print("Generated Token:", token)
print("Token verification:", jwt_auth.verify_token(token))

print("\n=== Session-based Authentication ===")
def session_auth_example():
    """Example of session-based authentication"""
    session = requests.Session()
    
    # Login and get session cookie
    login_data = {
        'username': 'user',
        'password': 'pass'
    }
    session.post('https://api.example.com/login', data=login_data)
    
    # Make authenticated requests using session
    response = session.get('https://api.example.com/protected')
    return response

print("\n=== Best Practices ===")
print("1. Never store credentials in code")
print("2. Use environment variables for sensitive data")
print("3. Implement token refresh mechanisms")
print("4. Use HTTPS for all authenticated requests")
print("5. Properly handle token expiration")
print("6. Securely store tokens and credentials")
print("7. Implement proper error handling")
print("8. Use established authentication libraries")