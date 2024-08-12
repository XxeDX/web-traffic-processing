import random
import pandas as pd
from datetime import datetime, timedelta

# Function to generate a random IP address
def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Function to generate a random timestamp within the last month
def generate_timestamp():
    start_date = datetime.now() - timedelta(days=30)
    random_date = start_date + timedelta(seconds=random.randint(0, 30 * 24 * 60 * 60))
    return random_date.strftime('%d/%b/%Y:%H:%M:%S')

# Function to generate a random HTTP request
def generate_request():
    method = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
    url = random.choice(['/home', '/about', '/contact', '/products', '/blog', '/login', '/signup'])
    http_version = random.choice(['HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0'])
    return f"{method} {url} {http_version}"

# Function to generate a random status code
def generate_status():
    return random.choice([200, 301, 400, 403, 404, 500, 502])

# Function to generate a random response size
def generate_size():
    return random.randint(200, 5000)

# Function to generate a random referrer
def generate_referrer():
    return random.choice([
        '-', 
        'https://www.google.com', 
        'https://www.bing.com', 
        'https://www.facebook.com', 
        'https://www.twitter.com', 
        'https://www.linkedin.com'
    ])

# Function to generate a random user-agent
def generate_user_agent():
    return random.choice([
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
    ])

# Generate the dataset
data = []

for _ in range(500):
    ip = generate_ip()
    timestamp = generate_timestamp()
    request = generate_request()
    status = generate_status()
    size = generate_size()
    referrer = generate_referrer()
    user_agent = generate_user_agent()
    
    log_entry = {
        "ip": ip,
        "timestamp": timestamp,
        "request": request,
        "status": status,
        "size": size,
        "referrer": referrer,
        "user_agent": user_agent
    }
    
    data.append(log_entry)

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("apache_access_log2.csv", index=False)

print("CSV file 'apache_access_log.csv' generated with 500 rows of data.")
