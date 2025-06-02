"""
Python API Integration Tutorial

This tutorial demonstrates how to integrate with various types of APIs.
Topics covered:
1. RESTful API integration
2. Pagination handling
3. Rate limiting
4. Data parsing and transformation
5. API wrappers
"""

import requests
import time
from datetime import datetime
import json

class APIClient:
    """Simple API client with rate limiting and error handling"""
    
    def __init__(self, base_url, rate_limit=60):
        self.base_url = base_url
        self.rate_limit = rate_limit  # requests per minute
        self.requests = []
    
    def _check_rate_limit(self):
        """Implement basic rate limiting"""
        now = datetime.now()
        # Remove requests older than 1 minute
        self.requests = [req_time for req_time in self.requests 
                        if (now - req_time).seconds < 60]
        
        if len(self.requests) >= self.rate_limit:
            print("Rate limit reached. Waiting...")
            time.sleep(60)
        
        self.requests.append(now)

    def get(self, endpoint, params=None):
        """Make a GET request with rate limiting"""
        self._check_rate_limit()
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None

print("\n=== Basic API Client Usage ===")
# Initialize client with JSONPlaceholder API
api_client = APIClient('https://jsonplaceholder.typicode.com')

# Fetch a post
print("Fetching post #1:")
post = api_client.get('/posts/1')
print(json.dumps(post, indent=2))

print("\n=== Handling Pagination ===")
def fetch_all_pages(api_client, endpoint, params=None):
    """Fetch all pages of paginated data"""
    if params is None:
        params = {}
    
    all_data = []
    page = 1
    
    while True:
        params['_page'] = page
        params['_limit'] = 10
        
        data = api_client.get(endpoint, params)
        
        if not data or len(data) == 0:
            break
            
        all_data.extend(data)
        page += 1
        
        # Stop after 3 pages for demonstration
        if page > 3:
            break
    
    return all_data

print("Fetching paginated posts:")
posts = fetch_all_pages(api_client, '/posts')
print(f"Total posts fetched: {len(posts)}")
print("First post:", json.dumps(posts[0], indent=2))

print("\n=== Data Transformation ===")
def transform_post_data(posts):
    """Transform API data into a different format"""
    transformed = []
    for post in posts:
        transformed.append({
            'title': post['title'].upper(),
            'body_preview': post['body'][:50] + '...',
            'word_count': len(post['body'].split())
        })
    return transformed

print("Transformed data:")
transformed_posts = transform_post_data(posts[:2])
print(json.dumps(transformed_posts, indent=2))

print("\n=== Implementing a Simple Cache ===")
class CachedAPIClient(APIClient):
    def __init__(self, base_url, rate_limit=60, cache_duration=300):
        super().__init__(base_url, rate_limit)
        self.cache = {}
        self.cache_duration = cache_duration
    
    def get(self, endpoint, params=None):
        """Get data from cache if available, otherwise from API"""
        cache_key = f"{endpoint}:{str(params)}"
        now = datetime.now()
        
        # Check cache
        if cache_key in self.cache:
            data, timestamp = self.cache[cache_key]
            if (now - timestamp).seconds < self.cache_duration:
                print("Returning cached data")
                return data
        
        # If not in cache or expired, fetch from API
        data = super().get(endpoint, params)
        if data:
            self.cache[cache_key] = (data, now)
        return data

print("\n=== Using Cached API Client ===")
cached_client = CachedAPIClient('https://jsonplaceholder.typicode.com')

print("First request (from API):")
data1 = cached_client.get('/posts/1')
print("Second request (from cache):")
data2 = cached_client.get('/posts/1')

print("\n=== Error Handling Patterns ===")
def robust_api_call(client, endpoint, max_retries=3, delay=1):
    """Make API calls with retry logic"""
    for attempt in range(max_retries):
        try:
            data = client.get(endpoint)
            if data:
                return data
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2  # Exponential backoff
    return None

print("Making robust API call:")
result = robust_api_call(api_client, '/posts/1')
if result:
    print("Success!")
    print(json.dumps(result, indent=2))

print("\n=== Best Practices ===")
print("1. Always implement rate limiting")
print("2. Use pagination for large datasets")
print("3. Implement caching when appropriate")
print("4. Handle errors gracefully")
print("5. Use retries with exponential backoff")
print("6. Transform data to match your needs")
print("7. Document your API integration")
print("8. Monitor API usage and responses")