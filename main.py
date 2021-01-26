import asyncio
import os
import pyppeteer


async def a_MakeScreenshot(url, selector=None, filename='screenshoot.png', path=None, res={'width': 1980, 'height': 1080}):
    if path is None:
        path = os.path.dirname(os.path.realpath(__file__))

    _file_path = os.path.join(path, filename)

    browser = await pyppeteer.launch()
    page = await browser.newPage()

    await page.setViewport(res)

    await page.goto(url)

    properties = {
        'path': _file_path,
        'omitBackground': True
        }

    if selector:
        bounding_box = await page.querySelector(selector)
        if bounding_box is None:
            raise KeyError(f'Element with selector "{selector}" not found!')
    else:
        bounding_box = page
        properties['fullPage'] = True

    await bounding_box.screenshot(properties)

    await browser.close()


def makeScreenshot(*args, **kwargs):
    asyncio.get_event_loop().run_until_complete(a_MakeScreenshot(*args, **kwargs))


if __name__ == '__main__':
    makeScreenshot('https://github.com/FlickDUB/Python_Web_Screenshoter', '#readme', filename='example.png')
