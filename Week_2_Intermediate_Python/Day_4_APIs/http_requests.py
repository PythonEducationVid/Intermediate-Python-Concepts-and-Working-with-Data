"""
Python HTTP Requests Tutorial

This tutorial covers making HTTP requests using the requests library.
Topics covered:
1. GET requests
2. Query parameters
3. Headers
4. Response handling
5. JSON responses
"""

import requests
import json

# Simple GET request
print("\n=== Basic GET Request ===")
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("\nResponse Content:")
print(json.dumps(response.json(), indent=2))

# GET request with query parameters
print("\n=== GET Request with Query Parameters ===")
params = {
    'postId': 1,
    '_limit': 3
}
response = requests.get(
    'https://jsonplaceholder.typicode.com/comments',
    params=params
)
print("URL with parameters:", response.url)
print("\nFirst comment:")
print(json.dumps(response.json()[0], indent=2))

# GET request with custom headers
print("\n=== GET Request with Custom Headers ===")
headers = {
    'User-Agent': 'Python Tutorial Bot',
    'Accept': 'application/json'
}
response = requests.get(
    'https://api.github.com/users/github',
    headers=headers
)
print("Response Status:", response.status_code)
if response.status_code == 200:
    print("\nGitHub User Info:")
    print(json.dumps(response.json(), indent=2))

# Error handling
print("\n=== Error Handling ===")
try:
    response = requests.get('https://httpbin.org/status/404')
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# Timeout handling
print("\n=== Timeout Handling ===")
try:
    response = requests.get('https://httpbin.org/delay/2', timeout=1)
    print("Response received!")
except requests.exceptions.Timeout:
    print("The request timed out")

# Session usage
print("\n=== Using Sessions ===")
with requests.Session() as session:
    # Session will remember cookies and keep the connection alive
    session.headers.update({'User-Agent': 'Python Tutorial Bot'})
    
    # Make multiple requests using the same session
    response1 = session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    response2 = session.get('https://httpbin.org/cookies')
    
    print("Cookies in session:", response2.json())

# Practical example: Fetching weather data
print("\n=== Practical Example: Weather API ===")
def get_weather(city, api_key='YOUR_API_KEY'):
    """
    Get weather data for a city using OpenWeatherMap API
    Note: Replace 'YOUR_API_KEY' with a real API key to make this work
    """
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"

# Example usage (will not work without API key)
print("Weather API example (simulation):")
weather_data = {
    "name": "London",
    "main": {
        "temp": 15.2,
        "humidity": 73
    },
    "weather": [{"description": "scattered clouds"}]
}
print(json.dumps(weather_data, indent=2))

# Best Practices Summary
print("\n=== Best Practices ===")
print("1. Always use try-except for error handling")
print("2. Set appropriate timeouts")
print("3. Use sessions for multiple requests")
print("4. Verify SSL certificates")
print("5. Check status codes")
print("6. Handle rate limiting")
print("7. Close responses with response.close()")
print("8. Use params instead of manually building URLs")