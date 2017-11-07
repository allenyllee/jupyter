// Puppeteer: a Node.js library to control headless Chrome | Our Code World
// https://ourcodeworld.com/articles/read/548/puppeteer-a-node-js-library-to-control-headless-chrome

// Require puppeteer
const puppeteer = require('puppeteer');

(async () => {
    // Create an instance of the chrome browser
    const browser = await puppeteer.launch();

    // Create a new page
    const page = await browser.newPage();

    // Set some dimensions to the screen
    page.setViewport({
        width: 1920,
        height: 1080
    });

    // Navigate to Our Code World
    await page.goto('http://ourcodeworld.com');

    // Create a screenshot of Our Code World website
    await page.screenshot({
        path: 'screenshot.png'
    });

    // Close Browser
    browser.close();
})();