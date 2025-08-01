# Subdomain Finder Tool

# What are subdomains?
    # - Subdomains are subdivisions of a main domain.
    #   For example, in blog.example.com, "blog" is the subdomain.
    # - Organizations often use subdomains to host different services or sections like:
    #     - admin.example.com (admin panel)
    #     - dev.example.com (development server)
    #     - mail.example.com (email service)

# Why perform subdomain enumeration?
    # Positive Uses (Defensive or Security Testing):
        # - Helps security teams identify all exposed services.
        # - Assists in inventory management of web applications.
        # - Finds forgotten, unused, or misconfigured subdomains.
        # - Useful for bug bounty hunters and penetration testers.

    # Negative Uses (Malicious Purposes):
        # - Attackers can use it to discover hidden or vulnerable endpoints.
        # - Subdomain takeover: If a subdomain points to a third-party service (e.g., GitHub Pages, Heroku) and the service is no longer claimed, attackers can hijack it.
        # - Phishing attacks: Fake login pages hosted on legitimate-looking subdomains can deceive users (e.g., secure-login.example.com).

# What is crt.sh?
    # - crt.sh is a public Certificate Transparency log search engine.
    # - It stores records of SSL/TLS certificates issued by Certificate Authorities (CAs).
    # - Subdomains that appear in SSL certificates are searchable using its API.

import requests
import sys

# Function to fetch subdomains from crt.sh for a given domain
def fetchDomains(domain):
    # Construct URL with URL-encoded %25. (This means %.example.com)
    url = f"https://crt.sh/search?q=%25.{domain}&output=json"

    try:
        # Send GET request to crt.sh with a timeout of 300 seconds
        response = requests.get(url, timeout=300)
        response.raise_for_status()  # Raise an error if response is not 200 OK

        # Parse JSON response
        data = response.json()

        # Use a set to store unique subdomains
        subdomains = set()

        # Iterate over each entry in the JSON data
        for entry in data:
            # Some entries may contain multiple names separated by newlines
            names = entry.get('name_value', "").split('\n')
            for name in names:
                name = name.strip()
                # Only include subdomains that contain the domain
                if domain in name:
                    subdomains.add(name)
        return subdomains

    except Exception as e:
        print(f"[!] Error: {e}")
        return []

# Entry point: script starts executing from here
if __name__ == "__main__":
    # Ensure the user provides exactly one argument (the domain name)
    if len(sys.argv) != 2:
        print("Usage: python SubDomainFinder.py <domain>")
        sys.exit(1)

    # Clean input: remove http://, https:// and any trailing slashes
    domain = sys.argv[1].replace("http://", "").replace("https://", "").strip('/')

    # Call the fetchDomains function
    SUBDOM = fetchDomains(domain)

    # Print subdomains if found
    if SUBDOM:
        print(f"\n[*] Subdomains for {domain}: \n")
        print("\n".join(SUBDOM))
    else:
        print("[!] No subdomains found.")
