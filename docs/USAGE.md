# Usage Examples

This document provides practical examples of using Python on Android with Sacred Smoke.

## Basic Python Scripts

### Hello World

```python
#!/usr/bin/env python3
# hello.py

print("Hello from Python on Android!")
```

Run it:
```bash
python3 hello.py
```

## Working with Files

### Reading and Writing Files

```python
#!/usr/bin/env python3
# file_operations.py

# Write to a file
with open('data.txt', 'w') as f:
    f.write('Hello from Android!\n')
    f.write('Python is running smoothly.\n')

# Read from a file
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)
```

### Working with JSON

```python
#!/usr/bin/env python3
# json_example.py

import json

# Create some data
data = {
    'device': 'Android',
    'python_version': '3.14.0',
    'architecture': 'aarch64'
}

# Write JSON to file
with open('config.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read JSON from file
with open('config.json', 'r') as f:
    loaded_data = json.load(f)
    print(f"Loaded: {loaded_data}")
```

## Network Operations

### Making HTTP Requests

```python
#!/usr/bin/env python3
# http_example.py

import urllib.request
import json

# Make a GET request
url = 'https://api.github.com/repos/python/cpython'
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())
    print(f"Repository: {data['name']}")
    print(f"Stars: {data['stargazers_count']}")
```

### Using requests library

First install requests:
```bash
python3 -m pip install requests
```

Then use it:
```python
#!/usr/bin/env python3
# requests_example.py

import requests

response = requests.get('https://api.github.com')
print(f"Status Code: {response.status_code}")
print(f"Headers: {response.headers['content-type']}")
```

## Data Processing

### Working with CSV

```python
#!/usr/bin/env python3
# csv_example.py

import csv

# Write CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '25', 'New York'],
    ['Bob', '30', 'San Francisco'],
    ['Charlie', '35', 'Seattle']
]

with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read CSV
with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(', '.join(row))
```

### Data Analysis with pandas

Install pandas:
```bash
python3 -m pip install pandas
```

Use it:
```python
#!/usr/bin/env python3
# pandas_example.py

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Seattle']
})

print(df)
print(f"\nAverage Age: {df['Age'].mean()}")
```

## Web Development

### Simple HTTP Server

```python
#!/usr/bin/env python3
# simple_server.py

from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello from Python on Android!</h1>')

with HTTPServer(('', PORT), MyHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()
```

Run it and access from a browser on the same network.

### Flask Web Application

Install Flask:
```bash
python3 -m pip install flask
```

Create a simple app:
```python
#!/usr/bin/env python3
# flask_app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Flask running on Android!</h1>'

@app.route('/api/info')
def info():
    return {
        'platform': 'Android',
        'python': '3.14.0',
        'framework': 'Flask'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## System Information

### Get Device Info

```python
#!/usr/bin/env python3
# device_info.py

import platform
import sys
import os

print("=== Python Information ===")
print(f"Python Version: {sys.version}")
print(f"Python Path: {sys.executable}")

print("\n=== Platform Information ===")
print(f"System: {platform.system()}")
print(f"Release: {platform.release()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")

print("\n=== Environment ===")
print(f"Current Directory: {os.getcwd()}")
print(f"User: {os.environ.get('USER', 'unknown')}")
print(f"Home: {os.environ.get('HOME', 'unknown')}")
```

## Database Operations

### SQLite Example

```python
#!/usr/bin/env python3
# sqlite_example.py

import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('myapp.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Insert data
cursor.execute('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)',
               ('Alice', 'alice@example.com'))
cursor.execute('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)',
               ('Bob', 'bob@example.com'))

conn.commit()

# Query data
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

conn.close()
```

## Automation Scripts

### Batch File Processing

```python
#!/usr/bin/env python3
# batch_process.py

import os
import glob

# Find all text files
text_files = glob.glob('*.txt')

for filename in text_files:
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Process: add line numbers
    output_filename = f'processed_{filename}'
    with open(output_filename, 'w') as f:
        for i, line in enumerate(lines, 1):
            f.write(f'{i}: {line}')
    
    print(f'Processed {filename} -> {output_filename}')
```

## Tips for Android Development

1. **Resource Management**: Be mindful of battery and memory usage
2. **Storage Paths**: Use appropriate storage locations for your app data
3. **Network Access**: Check connectivity before making network requests
4. **Permissions**: Some operations may require Android permissions
5. **Testing**: Test thoroughly on actual Android devices

## More Resources

- [Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python Tutorials](https://realpython.com/)

## Need More Examples?

Visit the [GitHub repository](https://github.com/scaredsmoke-star/Sacred-smoke) for more examples and community contributions.
