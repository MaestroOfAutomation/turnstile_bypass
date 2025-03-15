# turnstile_bypass

## Follow Me on Social Media
- **YouTube:** [Maestro Automation](https://www.youtube.com/@MaestroAutomation)
- **Telegram:** [Join the Channel](https://t.me/+mgOFDudWcTRmMTI0)

## Overview

This example demonstrates how to bypass Cloudflare Turnstile using Camoufox by simulating user actions on a webpage. Specifically, the script navigates to [dexscreener.com](https://dexscreener.com/), waits for the Cloudflare challenge iframe to appear, and then simulates a click on the checkbox by calculating its coordinates.

## What the Script Does

- **Navigate to the Website:** Uses `page.goto` to load dexscreener.com.
- **Wait for the Challenge to Load:** Implements a loop with a 1-second delay over 15 iterations to allow time for the page to load and the Cloudflare iframe to appear.
- **Search for the Cloudflare iframe:** Iterates over all frames on the page to identify the one with a URL starting with `https://challenges.cloudflare.com`.
- **Calculate Click Coordinates:** Once the correct frame is found, retrieves the frame element and its bounding box. The checkbox coordinates are then calculated using offsets from the frame's position.
- **Simulate the Click:** Uses the calculated coordinates to perform a mouse click, mimicking a user's click on the checkbox.

## Requirements

- Python 3.9 or higher
- An asynchronous library (e.g., `asyncio`)
- [Camoufox](https://playwright.dev/python/) or a similar browser automation tool (**must be undetected!**)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/MaestroOfAutomation/turnstile_bypass.git
   cd turnstile_bypass
2. **Install Dependencies:**

   ```
   pip install -r requirements.txt
   ```

## Running the Script
Run the script using:

```bash
python cloudflare_turnstile_bypass.py
```
Make sure your environment is properly configured to work with Camoufox if required for your use case.

## Code Explanation
Below is a snippet of the code with inline explanations:

```python
await page.goto("https://dexscreener.com/")

# Loop for waiting, allowing time for the Cloudflare iframe to appear
for _ in range(15):
    await asyncio.sleep(1)

    # Iterate over all frames on the page
    for frame in page.frames:
        # Check if the frame belongs to Cloudflare Turnstile
        if frame.url.startswith('https://challenges.cloudflare.com'):
            # Retrieve the frame element and its bounding box dimensions
            frame_element = await frame.frame_element()
            bounding_box = await frame_element.bounding_box()
            coord_x = bounding_box['x']
            coord_y = bounding_box['y']

            width = bounding_box['width']
            height = bounding_box['height']

            # Calculate the click coordinates for the checkbox
            checkbox_x = coord_x + width / 9
            checkbox_y = coord_y + height / 2

            # Simulate a mouse click at the calculated coordinates
            await page.mouse.click(x=checkbox_x, y=checkbox_y)
```

## Important Note
This example is provided solely for educational purposes. Use this code responsibly and in compliance with legal requirements and the terms of service of the targeted websites. Bypassing security measures can be illegal or violate site policies.

   
