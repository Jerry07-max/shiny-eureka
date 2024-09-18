import requests

# URL of the frontend service running on Minikube (replace with different IP and Port as required)
Frontend_URL = "http://127.0.0.1:52336"

# Expected response from the backend
Expected_message = "Hello from the Backend!" # Update if the message is something else.

def test_frontend_backend_integration():
    try:
        # Sending a GET request to frontend
        response = requests.get(Frontend_URL, timeout = 10)

        # Checking whether the request was successful
        assert response.status_code == 200, f"Failed! Status code: {response.status_code}"

        # Checking whether the frontend is displaying the expected message from the backend
        assert Expected_message in response.text, f"Failed! Expected message not found in response: {response.text}"

        print("Success! Frontend is displaying the correct message from the backend.")
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except AssertionError as e:
        print(f"Test failed: {e}")

# Run the test
if __name__ == "__main__":
    test_frontend_backend_integration()
