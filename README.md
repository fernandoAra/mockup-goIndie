# goIndie Mockup

This repository contains the code for the mockup of the goIndie platform, a project that aims to promote indie artists by recommending them to listeners based on their music preferences. The mockup currently includes a basic web interface, which allows users to input their favorite artists and receive manually curated recommendations. The final version of the project will incorporate AI-driven recommendations based on user input.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)

## Features
- A simple homepage to introduce the user to the platform.
- An artist input page for users to provide their favorite artists or songs.
- A recommendation page that displays indie artists based on manually curated data.
- The visual size of artist images corresponds to their relevance or popularity.

## Requirements
- Python 3.8 or above
- Flask
- Tailwind CSS (CDN used, no local installation required)

## Installation

1. Clone the repository to your local machine:
   ```
   bash
   git clone https://github.com/yourusername/goIndie-mockup.git
   cd goIndie-mockup
   ```
2. It is recommended to set up a virtual environment (optional):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```
   pip install flask
   ```
## Running the Project

1. Navigate to the project directory and ensure all dependencies are installed.
2. Run the Flask development server:
  ```
  bash
  flask run
  ```
4. Open your web browser and go to http://127.0.0.1:5000/ to access the website.

## Project Structure
```
goIndie-mockup/
│
├── app.py                  # Flask application
├── templates/              # HTML templates
│   ├── home.html           # Homepage
│   ├── input.html          # Artist input page
│   └── recommendations.html# Recommendation results page
├── static/                 # (optional) Static files (CSS, JS, images)
├── venv/                   # (optional) Virtual environment
└── README.md               # This file
```

## Customization

If you wish to customize the recommendation logic, you can manually edit the app.py file. The recommendations in the current mockup are hard-coded and can be changed based on your needs. Future updates will integrate AI-driven recommendations.

## License

This project is licensed under the MIT License. See the [LICENSE](#license) file for details.
