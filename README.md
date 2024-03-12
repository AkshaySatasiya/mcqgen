# 📚 MCQ Generator Application with Langchain

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python version" />
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License" />
</p>

## Description

This repository contains a Python application for generating multiple-choice questions (MCQs) using Langchain. The MCQs are created based on input text, allowing customization for different subjects and complexity levels.

## 🎯 Getting Started

Clone the Repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

## 🛠️ Environment Setup:

Create a virtual environment (optional but recommended).
Install the dependencies using the command mentioned in the Installation section.

## 🚀 Installation

To run the MCQ Generator application, ensure you have the required dependencies installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup:

Obtain an API key from OpenAI and set it as an environment variable in a .env file.

## ▶️ Run the Streamlit App:

```bash
streamlit run StreamlitAPP.py
```

## 🚀 Usage

### 1. File Upload:

- Upload a PDF or text file containing the input text for MCQ generation.

### 2. Input Fields:

- Specify the number of MCQs, subject, and the complexity level of questions.

### 3. Generate MCQs:

- Click the "Create MCQs" button to generate the MCQs based on the provided inputs.

### 4. Review Generated MCQs:

- View the generated MCQs in a table format along with a review in the Streamlit app.

## 📁 File Descriptions

### 1. StreamlitAPP.py:

- Main script containing the Streamlit application for the MCQ Generator.

### 2. mcqgenerator.py:

- Script handling the generation and evaluation of MCQs using Langchain.

### 3. logger.py:

- Logging setup to record application events.

### 4. utils.py:

- Utility functions for reading files and extracting table data from the generated MCQs.

### 5. requirements.txt:

- List of required Python packages for the application.

## 📝 Logging

Application events are logged in the logs directory. Each log file is timestamped for easy reference.

## 🙌 Acknowledgments

The MCQ Generator application utilizes the Langchain library and OpenAI API for natural language processing.

## 🤝 Contribution

Contributions are welcome! Please read the contribution guidelines before submitting a pull reques

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

---

Feel free to reach out for any queries or support regarding this project.

Happy Coding! 🚀
