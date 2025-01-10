import requests
import re
import hashlib

URL = ""

def solve_challenge():
    try:
        # Use a session for faster connection reuse
        with requests.Session() as session:
            # Step 1: Fetch the challenge page
            response = session.get(URL, timeout=2)
            if response.status_code != 200:
                print(f"Error: Unable to fetch the page. Status Code: {response.status_code}")
                return
            
            print("Response from server")
            print(response.text)
	
            
            # Step 2: Extract the string using regex
            # This avoids using BeautifulSoup for parsing and speeds up the script
            match = re.search(r"<h3[^>]*>(.*?)</h3>", response.text)
            if not match:
                print("Error: Unable to find the string in the response.")
                return
            
            string_to_hash = match.group(1).strip()
            print(f"String to hash: {string_to_hash}")

            # Step 3: Compute the MD5 hash
            md5_hash = hashlib.md5(string_to_hash.encode()).hexdigest()
            print(f"Computed MD5 hash: {md5_hash}")

            # Step 4: Submit the hash
            data = {"hash": md5_hash}
            submission_response = session.post(URL, data=data, timeout=2)

            # Step 5: Display the result
            if submission_response.status_code == 200:
                print("Response received!")
                print(submission_response.text)
            else:
                print(f"Failed to submit hash. Status Code: {submission_response.status_code}")
                print(submission_response.text)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    solve_challenge()
