# Test Automation QA - BEES Marketplace

### About this Project

This project automates test scenarios for the proposed challenge, there are some frontend and backend tests.

The test automation project was created using Python, Cucumber, Requests, and Selenium webdriver. It follows the Page Object Model (POM) pattern for browser tests.
<br>
<br>

### Local Installation Guide
1. Clone this project with git clone `https://github.com/LeandroStevanatoAlves/test_bees.git`
2. Install **Python** and **Pip**
3. Navigate to the project folder and install dependencies with `pip install -r requirements.txt`
4. Run tests with `behave -f html -o behave-report.html`
5. An HTML execution report named **behave-report.html** will be created in the project's root. If the report already exists, it will be overwritten.
<br>
<br>

### Continuous Integration
The project has a configured pipeline in **GitHub Actions**. When runs in the pipeline, Chromedriver automatically switches to headless mode.
<br>
<br>

### Observations
The project ended up being quite extensive, so I didn't explore more test scenarios.

There is still plenty of room for code optimization, especially in API tests.

I aimed to follow best practices and kept the tests self-contained, creating and deleting all necessary data at the end of each test.
