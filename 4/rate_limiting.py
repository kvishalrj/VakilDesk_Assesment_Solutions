import time
import threading

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests  # Max requests allowed per user
        self.time_window = time_window  # Time window in seconds (1 minute)
        self.requests = {}  # Dictionary to store user requests (user_id -> list of timestamps)
        self.lock = threading.Lock()  # Lock to ensure thread-safe access

    def allow_request(self, user_id):
        """Check if a request is allowed for the given user."""
        current_time = time.time()

        with self.lock:  # Ensure thread safety when modifying shared resources
            if user_id not in self.requests:
                self.requests[user_id] = []

            # Filter out requests that are outside the time window (older than 1 minute)
            self.requests[user_id] = [req_time for req_time in self.requests[user_id] if current_time - req_time < self.time_window]

            # Check if the user has exceeded the request limit
            if len(self.requests[user_id]) < self.max_requests:
                # Allow the request and log the current request time
                self.requests[user_id].append(current_time)
                return True
            else:
                # Deny the request if the limit is exceeded
                return False


if __name__ == "__main__":
    rate_limiter = RateLimiter(max_requests=5, time_window=60)

    user_id = "user_123"

    for i in range(7):  # Simulate 7 requests
        if rate_limiter.allow_request(user_id):
            print(f"Request {i+1}: Allowed")
        else:
            print(f"Request {i+1}: Denied")

        # Simulate a small time gap between requests
        time.sleep(10)


# Expected output --------------------

# Request 1: Allowed
# Request 2: Allowed
# Request 3: Allowed
# Request 4: Allowed
# Request 5: Allowed
# Request 6: Denied
# Request 7: Allowed