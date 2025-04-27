const puppeteer = require('puppeteer');
const axios = require('axios');

const FRONTEND_URL = 'http://localhost:3003';
const API_URL = 'http://localhost:8000';

const TEST_EPISODE = {
  name: 'Automated Regression Test Episode',
  episode_body: '# Test Episode\nThis episode is injected by the regression test.',
  group_id: 'regression-suite',
  source: 'markdown',
  source_description: 'Automated regression test'
};

async function seedBackend() {
  try {
    await axios.post(`${API_URL}/episode`, TEST_EPISODE);
    console.log('✅ Seeded backend with test episode.');
  } catch (e) {
    console.error('❌ Failed to seed backend:', e.response?.data || e.message);
    process.exit(1);
  }
}

async function runUITest() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(FRONTEND_URL, { waitUntil: 'networkidle2' });

  // Wait for the search input
  await page.waitForSelector('input[type="text"]');
  await page.type('input[type="text"]', 'Test Episode');

  // Click the search button
  await page.waitForSelector('button[type="submit"]');
  await page.click('button[type="submit"]');

  // Wait for results to appear
  await page.waitForTimeout(1500);

  // Take screenshot
  await page.screenshot({ path: 'ui_regression_result.png', fullPage: true });

  // Check for the test episode in results
  const found = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.MuiListItemText-root')).some(node => node.textContent.includes('Test Episode'));
  });

  if (found) {
    console.log('✅ UI regression test passed: Test episode found in search results.');
  } else {
    console.error('❌ UI regression test failed: Test episode NOT found in search results.');
    process.exit(1);
  }

  await browser.close();
}

(async () => {
  await seedBackend();
  await runUITest();
})();
