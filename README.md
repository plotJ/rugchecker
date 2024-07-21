# Token Security Analyzer using rugcheck.xyz

## About
This Python script is designed to analyze the security of cryptocurrency tokens using the rugcheck.xyz platform. It demonstrates web scraping techniques to extract security-related information about tokens, providing insights into potential risks and vulnerabilities.

## Features
- Analyzes token security using rugcheck.xyz
- Extracts key security metrics including security score, liquidity information, and contract verification status
- Identifies and compiles security warnings
- Provides a structured output of the security analysis

## Technologies Used
- Python 3
- Requests library for making HTTP requests
- BeautifulSoup4 for web scraping and HTML parsing
- JSON for data formatting

## How It Works
1. The script takes a token address as input.
2. It sends a request to rugcheck.xyz with the token address.
3. The HTML response is parsed to extract relevant security information.
4. The script compiles the extracted data into a structured format.
5. Results are presented in a JSON format for easy reading and further processing.

## Prerequisites
- Python 3.7+
- Internet connection to access rugcheck.xyz

## Installation and Usage
1. Clone this repository
2. Install required libraries:
   pip install requests beautifulsoup4
3. Run the script:
   python rugcheck.py
4. When prompted, enter the token address you wish to analyze

## Sample Output
{
  "token_address": "0x1234567890abcdef1234567890abcdef12345678",
  "security_score": "85/100",
  "liquidity_info": "Locked for 365 days",
  "contract_verification": "Verified",
  "warnings": [
    "High total supply",
    "New token (less than 30 days old)"
  ]
}

## Limitations
- This script relies on the structure of rugcheck.xyz remaining consistent. Changes to their website may require updates to the scraping logic.
- The accuracy of the analysis depends on the data provided by rugcheck.xyz.
- Web scraping may be against the terms of service of some websites. Always ensure you have permission to scrape data.

## Future Enhancements
- Implement error handling for network issues or changes in website structure
- Add support for batch analysis of multiple tokens
- Integrate with other security analysis platforms for comprehensive results
- Develop a user interface for easier interaction and data visualization

## Ethical Considerations
This tool is designed for educational and research purposes. Users should respect the terms of service of rugcheck.xyz and use the data responsibly. This tool should not be used as the sole basis for investment decisions.

## Contribution
Contributions to this project are welcome! Feel free to fork the repository and submit pull requests with improvements or additional features.

## License
This project is open source and available under the [MIT License](LICENSE).

---

Created by Josh Plotkin
