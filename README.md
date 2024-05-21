# K-12 Education Analytics

## Project Overview

This project aims to analyze a dataset of student performance and demographics to provide insights into student achievement, attendance, and demographics. The goal is to uncover trends and correlations that can inform educational strategies and interventions, ultimately improving student outcomes.

## Table of Contents

1. [Introduction](#introduction)
2. [Business Questions](#business-questions)
3. [Data Description](#data-description)
4. [Installation](#installation)

## Introduction

In the K-12 educational system, understanding student demographics and performance is crucial for developing effective educational strategies. This project analyzes synthetic data representing various aspects of student demographics and performance, including attendance and scores in core subjects.

## Business Questions

1. What are the demographic characteristics of the student population?
2. How does attendance vary among different demographics?
3. What are the trends in student performance across different subjects?
4. Are there any correlations between student demographics and performance?

## Data Description

The dataset is synthetic and generated using the `generate_sample_data.py` script. It includes the following columns:

- **Student_ID:** Unique identifier for each student
- **Gender:** Gender of the student (Male/Female)
- **DOB:** Date of Birth of the student
- **Grade:** Grade level (1 to 12)
- **Attendance:** Attendance percentage
- **Math_Score:** Math score (50 to 100)
- **Reading_Score:** Reading score (50 to 100)
- **Science_Score:** Science score (50 to 100)
- **Age:** Calculated age from DOB

## Installation

To run this project, you need to have Python installed along with the required libraries. You can install the necessary libraries using the following command:

```bash
pip install pandas numpy faker matplotlib seaborn
'''


