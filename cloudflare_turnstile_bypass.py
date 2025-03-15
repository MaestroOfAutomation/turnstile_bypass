import asyncio

from browserforge.fingerprints import Screen
from camoufox.async_api import AsyncCamoufox


async def cloudflare_bypass_example():
    async with AsyncCamoufox(
            headless=False,
            os=["macos"],
            screen=Screen(max_width=1920, max_height=1080),
    ) as browser:
        page = await browser.new_page()
        await page.goto("https://dexscreener.com/")

        for _ in range(15):
            await asyncio.sleep(1)

            for frame in page.frames:
                if frame.url.startswith('https://challenges.cloudflare.com'):
                    frame_element = await frame.frame_element()
                    bounding_box = await frame_element.bounding_box()
                    coord_x = bounding_box['x']
                    coord_y = bounding_box['y']

                    width = bounding_box['width']
                    height = bounding_box['height']

                    checkbox_x = coord_x + width / 9
                    checkbox_y = coord_y + height / 2

                    await page.mouse.click(x=checkbox_x, y=checkbox_y)

        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(cloudflare_bypass_example())
