# 🏢 Property Diagnostics AI

## Overview

Property Diagnostics AI is an AI-powered application that automates the analysis of property inspection reports and thermal inspection reports. The system extracts text and images from PDF documents, analyzes the findings, and issue summaries, probable root causes, severity assessments, and recommended actions.

---

## Problem Statement

Property inspection reports and thermal reports often require manual review by engineers and inspectors. This process can be time-consuming and prone to inconsistencies.

This project automates the workflow by:

* Processing Inspection Report PDFs
* Processing Thermal Report PDFs
* Extracting observations and thermal finding


### PDF Processing

* Upload Inspection Report PDF
* Upload Thermal Report PDF
* Extract text using PyMuPDF


### Image Extraction

* Extract thermal images from reports
* Store extracted images for review

### AI-Based Report Generation

* Property Issue Summary
* Area-wise Observations
* Probable Root Cause Analysis
* Severity Assessment
* Recommended Actions
* Missing Information Detection

### User Interface

* Built using Streamlit
* Simple upload-and-generate workflow

---

## Project Architecture

Inspection Report PDF
+
Thermal Report PDF

↓

Document Processing

↓

Text & Image Extraction

↓

AI Reasoning Engine

↓

DDR Generation

↓

Final Report Output


## Tech Stack


 Python                  
 Streamlit                
 PyMuPDF                  
 Pillow                   
 ReportLab                


## Project Structure

Property_Diagnostics_AI/

├── app.py

├── document_parser.py

├── image_extractor.py

├── reasoning.py

├── prompts.py

├── requirements.txt

├── README.md

 
#How System work
1. Upload Inspection Report PDF
2. Upload Thermal Report PDF
3. Extract text and images
4. Analyze observations and findings




