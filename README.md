# hyperface-assignment



📘 Amazon UI Automation – Playwright (Python + Pytest)



This project automates an end-to-end Amazon user journey using Playwright (Python, Async) and Pytest, following a clean Page Object Model (POM) structure.



📂 Project Structure

hyperface-assignment/

│

├── constants/

│   ├── amazon\_constants.py

│

├── pages/

│   ├── home\_page.py

│   ├── results\_page.py

│   ├── product\_page.py

│   ├── cart\_page.py

│

├── tests/

│   ├── test\_amazon\_end\_to\_end\_experience.py

│

├── utils/

│   ├── playwright.config.py

│

├── reports/

│   ├── report.html   (generated after test execution)

│

├── .venv/            (Python virtual environment)

│

├── pytest.ini

├── requirements.txt

├── README.md         (this file)





⚙️ Installation \& Setup

1️⃣ Create Virtual Environment

python -m venv .venv





Activate the environment:



Windows PowerShell:

.\\.venv\\Scripts\\activate



2️⃣ Install Dependencies



Install required packages:



pip install pytest pytest-asyncio pytest-base-url allure-pytest playwright





Install Playwright browsers:



playwright install



3️⃣ Pytest Configuration (pytest.ini)



Your existing config:



\[pytest]

addopts = -s -v

testpaths = tests

python\_files = test\_\*.py

asyncio\_mode = auto





This enables:

✔ Async test support

✔ Auto detection of async fixtures

✔ Test discovery under tests/







🚀 Running Tests

Run complete test suite

pytest



Run tests with HTML Report

pytest --html=reports/report.html





After execution, open:



reports/report.html







📑 Test Case Coverage

Test Name: Amazon End-to-End User Journey



This test automates the full shopping flow on Amazon.



TC\_001 – Validate Launch Amazon \& Search Product



Launch Amazon homepage



Validate page load



Search for the default product



Example: "laptop"



TC\_002 – Apply Filters



Filter by brand



Filter by price range



Example: "HP", "₹25,000 – ₹35,000"



TC\_003 – Open First Product



Open the first product from search results



Switch to the new tab



Validate product page load



TC\_004 – Add Product to Cart



Click “Add to Cart”



Navigate to cart



Validate:



Product title exists



Quantity > 0



Price is displayed





🧩 Page Object Model (POM) Structure

✔ HomePage



launch\_site()



search\_product()



✔ ResultsPage



apply\_filters()



open\_first\_product()



✔ ProductPage



add\_to\_cart()



✔ CartPage



validate\_cart()



Each page class has:



Locators



Page-specific actions



No test logic inside pages



Test file remains clean and readable.







📦 Requirements File (recommended)



Create requirements.txt:



pytest

pytest-asyncio

pytest-base-url

allure-pytest

playwright





Install using:



pip install -r requirements.txt







📊 HTML Report



After running:



pytest --html=reports/report.html





You get a detailed report containing:



Test status (PASS/FAIL)



Execution time



Logs (due to -s)



Error trace \& screenshots (if implemented later)







✔ Final Notes



Fully async Playwright implementation



Clean Page Object Model



Organized constants \& utilities



Supports HTML reporting



Lightweight, scalable, and interview-ready framework

