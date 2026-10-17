

import time

# Get the current Unix timestamp
timestamp = time.time()

# Format the current date
current_date = time.strftime("%b %d %Y", time.localtime(timestamp))

# Display the results
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or",
      f"{timestamp:.2e} in scientific notation")
print(current_date)
