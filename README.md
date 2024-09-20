# Assessment Solutions

This repository contains solutions to the assessment questions, which involve web scraping, data processing, Django models, rate limiting, data aggregation, and finding duplicates in an array.

## Requirements

- Python 3.8 or higher
- Libraries: 
  - Django==4.1.3
  - beautifulsoup4==4.12.0
  - requests==2.28.1
  - pandas==1.5.2


## Solutions

### Q1: Web Scraping

A Python script that scrapes the titles and URLs of the latest articles from a news website (CNN, etc.) using BeautifulSoup and requests. See folder `1`.

### Q2: CSV Data Cleaning

A Python script that reads a CSV file with user data, removes duplicate entries based on user_id, filters out rows with invalid email formats, and writes the cleaned data to a new CSV file. See folder `2`.

### Q3: Django Model Method

A method to get the top 5 customers who have spent the most in the last 6 months, using a Django model with fields customer, order_date, status, and total_amount. Example view included. See folder `3`.

### Q4: Rate Limiter Implementation

Implementation of a rate limiter in Python that allows a maximum of 5 requests per minute per user, including concurrency handling. See folder `4`.

### Q5: Data Aggregation Function

A function that aggregates values from a list of dictionaries, grouping by a provided key and applying an aggregator function without using built-in groupby methods. See folder `5`.

### Q6: Find Duplicate in Array

A solution to find a duplicate number in an array of n+1 integers where each integer is between 1 and n, using O(1) extra space. See folder `6`.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kvishalrj/VakilDesk_Assesment_Solutions.git
   cd VakilDesk_Assesment_Solutions
   ```

2. **Install Dependencies**:
   Make sure to install the required libraries. Create a virtual environment if needed, and run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Individual Scripts**:
   - For Q1, navigate to folder `1` and run:
     ```bash
     python web_scraping.py
     ```
   - For Q2, navigate to folder `2` and run:
     ```bash
     python data_processing.py
     ```
   - For Q3, navigate to folder `3`, ensure Django is set up and migrations are applied, then run the server:
     ```bash
     python manage.py runserver
     ```
   - For Q4, navigate to folder `4` and run:
     ```bash
     python rate_limiting.py
     ```
   - For Q5, navigate to folder `5` and run:
     ```bash
     python data_aggregation.py
     ```
   - For Q6, navigate to folder `6` and run:
     ```bash
     python finding_duplicates.py
     ```

## Submission Guidelines

1. Submit the assessment test within 3 days of receipt of this assignment.
2. Make the repository public and share the working link to the repository.
3. Ensure the `requirements.txt`, migrations (for Django), and this README are included.
4. Make sure that all steps to set up and run the project are clearly documented.
