"""
Python API Error Handling Tutorial

This tutorial covers common error handling patterns when working with APIs:
1. HTTP status codes
2. Exception handling
3. Retry mechanisms
4. Logging errors
5. Custom error classes
"""

import requests
import time
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Custom API Exception
class APIError(Exception):
    """Custom exception for API errors"""
    def __init__(self, message, status_code=None, response=None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)

print("\n=== Basic Error Handling ===")
# Handling different HTTP status codes
def handle_response(response):
    """Handle different HTTP status codes"""
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise APIError("Resource not found", status_code=404)
    elif response.status_code == 401:
        raise APIError("Unauthorized access", status_code=401)
    elif response.status_code == 429:
        raise APIError("Rate limit exceeded", status_code=429)
    else:
        raise APIError(f"API error occurred: {response.status_code}", 
                      status_code=response.status_code)

# Example usage
print("Trying different URLs:")
urls = [
    'https://jsonplaceholder.typicode.com/posts/1',  # Valid
    'https://jsonplaceholder.typicode.com/posts/999',  # Not found
    'https://api.github.com/user'  # Unauthorized
]

for url in urls:
    try:
        response = requests.get(url)
        data = handle_response(response)
        print(f"Success for {url}")
        print(data)
    except APIError as e:
        print(f"Error for {url}: {e.message} (Status: {e.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")

print("\n=== Retry Mechanism ===")
def retry_request(url, max_retries=3, delay=1):
    """Make a request with retry logic"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay * (attempt + 1))  # Exponential backoff
            else:
                logger.error(f"All retries failed for {url}")
                raise

print("Testing retry mechanism:")
try:
    data = retry_request('https://httpbin.org/status/500')
except requests.exceptions.RequestException as e:
    print(f"Final error: {e}")

print("\n=== Rate Limiting Handler ===")
class RateLimitHandler:
    def __init__(self, requests_per_minute):
        self.requests_per_minute = requests_per_minute
        self.requests = []

    def wait_if_needed(self):
        """Wait if rate limit is reached"""
        now = datetime.now()
        minute_ago = now.timestamp() - 60
        
        # Remove old requests
        self.requests = [req for req in self.requests if req > minute_ago]
        
        if len(self.requests) >= self.requests_per_minute:
            wait_time = 60 - (now.timestamp() - self.requests[0])
            print(f"Rate limit reached. Waiting {wait_time:.2f} seconds...")
            time.sleep(wait_time)
        
        self.requests.append(now.timestamp())

# Example usage of rate limit handler
rate_limiter = RateLimitHandler(requests_per_minute=2)
print("Testing rate limiting:")
for i in range(3):
    rate_limiter.wait_if_needed()
    print(f"Making request {i+1}")
    time.sleep(0.1)  # Simulate request

print("\n=== Comprehensive Error Handling Example ===")
def make_api_request(url, method='get', **kwargs):
    """
    Make an API request with comprehensive error handling
    """
    try:
        # Prepare the request
        request_func = getattr(requests, method.lower())
        
        # Add timeout
        kwargs.setdefault('timeout', 10)
        
        # Make the request
        response = request_func(url, **kwargs)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse response
        return response.json()
    
    except requests.exceptions.Timeout:
        logger.error(f"Request to {url} timed out")
        raise APIError("Request timed out")
    
    except requests.exceptions.ConnectionError:
        logger.error(f"Connection error for {url}")
        raise APIError("Could not connect to server")
    
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
        raise APIError(f"HTTP error: {e}", 
                      status_code=e.response.status_code,
                      response=e.response)
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        raise APIError(f"Request failed: {e}")
    
    except ValueError as e:
        logger.error(f"Error parsing JSON response: {e}")
        raise APIError("Invalid JSON response")

# Example usage
print("Testing comprehensive error handling:")
try:
    data = make_api_request('https://jsonplaceholder.typicode.com/posts/1')
    print("Success:", data)
except APIError as e:
    print(f"Error: {e.message}")

print("\n=== Best Practices ===")
print("1. Always use try-except blocks")
print("2. Implement retry mechanisms")
print("3. Use rate limiting")
print("4. Log errors properly")
print("5. Create custom exception classes")
print("6. Handle different HTTP status codes")
print("7. Implement timeout handling")
print("8. Use proper error messages")