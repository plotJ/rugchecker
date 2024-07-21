import requests
from bs4 import BeautifulSoup
import json

def analyze_token_security(token_address):
    # Base URL for the rugcheck.xyz site
    base_url = "https://rugcheck.xyz"
    
    # Construct the URL for the token check
    check_url = f"{base_url}/tokens/{token_address}"
    
    try:
        # Send a GET request to the URL
        response = requests.get(check_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant information
        # Note: These selectors are hypothetical and would need to be adjusted based on the actual structure of the website
        security_score = soup.select_one('.security-score').text
        liquidity_info = soup.select_one('.liquidity-info').text
        contract_verification = soup.select_one('.contract-verification').text
        
        # You might also want to check for specific security flags or warnings
        warnings = [warning.text for warning in soup.select('.warning')]
        
        # Compile the results
        analysis_result = {
            "token_address": token_address,
            "security_score": security_score,
            "liquidity_info": liquidity_info,
            "contract_verification": contract_verification,
            "warnings": warnings
        }
        
        return analysis_result
    
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

def main():
    token_address = input("Enter the token address to analyze: ")
    result = analyze_token_security(token_address)
    
    if result:
        print(json.dumps(result, indent=2))
    else:
        print("Failed to analyze token security.")

if __name__ == "__main__":
    main()