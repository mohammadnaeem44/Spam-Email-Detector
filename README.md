# Email Spam Detection System

## Overview

The Email Spam Detection System is a Machine Learning-based web application that classifies email content as **Spam** or **Not Spam (Ham)**. The system leverages Natural Language Processing (NLP) techniques and a Multinomial Naive Bayes classifier to analyze email text and predict whether it is legitimate or spam.

The application is developed using Flask, providing an intuitive web interface where users can paste email content and instantly receive classification results.

---

## Features

* Detects spam and non-spam emails.
* Text preprocessing and feature extraction using TF-IDF Vectorization.
* Machine Learning-based classification using Multinomial Naive Bayes.
* User-friendly web interface built with Flask.
* Fast and lightweight prediction system.
* Easy deployment and scalability.

---

## Project Structure

```text
spam-email-detector/
│
├── dataset/
│   └── spam.csv
│
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* Pickle
* HTML5
* CSS3

---

## Machine Learning Pipeline

### 1. Data Collection

The project uses an Email Spam Dataset containing labeled email messages.

### 2. Data Preprocessing

* Remove unnecessary columns.
* Extract email text.
* Encode labels into numerical values.
* Prepare data for model training.

### 3. Feature Engineering

* Convert email text into numerical vectors using TF-IDF Vectorization.

### 4. Model Training

* Split dataset into training and testing sets.
* Train a Multinomial Naive Bayes classifier.
* Evaluate model performance.

### 5. Model Deployment

* Save trained model and vectorizer using Pickle.
* Deploy using Flask for real-time predictions.

---

## Dataset Information

The dataset consists of email messages labeled as spam or ham.

### Columns

| Column    | Description                        |
| --------- | ---------------------------------- |
| label     | Email category (spam/ham)          |
| text      | Email content                      |
| label_num | Numerical representation of labels |

### Dataset Size

* Total Records: 5,171 Emails
* Classes:

  * Spam
  * Ham (Not Spam)

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/spam-email-detector.git
cd spam-email-detector
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train the Model

```bash
python train_model.py
```

Expected Output:

```text
Model trained successfully!
```

---

## Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Example

### Input Email

```text
Congratulations!

You have been selected to receive a free gift voucher worth $1000.

Click the link below to claim your reward immediately.
```

### Prediction

```text
Spam Email
```

---

## Future Improvements

* Spam probability score (% confidence).
* Prediction history storage using SQLite.
* REST API support.
* Advanced NLP preprocessing.
* Deep Learning-based spam detection.
* Docker containerization.
* Cloud deployment using Render or AWS.

---

## Learning Outcomes

This project demonstrates:

* Natural Language Processing (NLP)
* Text Classification
* Machine Learning Model Training
* Model Serialization with Pickle
* Flask Web Development
* End-to-End ML Deployment

---

## Author

**Mohammad Naeem**

Bachelor of Engineering

Sukkur IBA University

---
📬 Contact

📧 mohammadnaeem.cse@gmail.com
🔗 linkedin.com/in/mohammad-naeem
🐙 github.com/mohammadnaeem44

## License

This project is developed for educational and  academic purpose.
