# -*- coding: utf-8 -*-
"""Inference_CareerCompas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CJJfJOS2qPru9v--rDKOlwknw11F13V3
"""

pip install pandas numpy tensorflow pymupdf

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re

# ✅ Download dulu data yang diperlukan
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

import fitz  # PyMuPDF
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf
import re
import string

from tensorflow.keras.preprocessing.sequence import pad_sequences

from google.colab import drive
drive.mount('/content/drive')

# =============================
# CONFIGURATION
# =============================

MAX_LEN = 200  # Sesuaikan dengan saat training
TOP_N = 20      # Jumlah rekomendasi teratas

# =============================
# FUNGSI PREPROCESSING
# =============================

def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\n|\r|\t', ' ', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words and len(w) > 1]
    tokens = [lemmatizer.lemmatize(w) for w in tokens]
    return " ".join(tokens)

# =============================
# EKSTRAKSI TEKS DARI PDF
# =============================

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

# =============================
# LOAD TOKENIZER & MODEL
# =============================

with open("/content/drive/MyDrive/Capstone - Career Compas/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

model = tf.keras.models.load_model("/content/drive/MyDrive/Capstone - Career Compas/jobmatch_model.h5")

# =============================
# LOAD DATA JOBS
# =============================

jobs_df = pd.read_csv("/content/drive/MyDrive/Capstone - Career Compas/jobdesc_clean.csv")
jobs_df['job_text'] = jobs_df['Job Description'].apply(preprocess_text)

# =============================
# PREDIKSI DAN REKOMENDASI
# =============================

def get_recommendations(resume_text, top_n=TOP_N):
    resume_clean = preprocess_text(resume_text)

    # Tokenisasi dan padding
    resume_seq = tokenizer.texts_to_sequences([resume_clean])
    resume_pad = pad_sequences(resume_seq, maxlen=MAX_LEN, padding="post")

    job_seqs = tokenizer.texts_to_sequences(jobs_df['job_text'])
    job_pad = pad_sequences(job_seqs, maxlen=MAX_LEN, padding="post")

    # Duplikat resume sebanyak jumlah job
    resume_batch = np.repeat(resume_pad, len(job_pad), axis=0)

    # Prediksi kecocokan
    predictions = model.predict([resume_batch, job_pad], verbose=0).flatten()

    jobs_df["match_score"] = predictions
    top_jobs = jobs_df.sort_values("match_score", ascending=False).head(top_n)

    return top_jobs[['Job Title','skills', 'Company', 'match_score']]

# =============================
# MAIN
# =============================

if __name__ == "__main__":
    pdf_path = "/content/drive/MyDrive/Capstone - Career Compas/cv/cv1.pdf"  # file resume PDF
    resume_text = extract_text_from_pdf(pdf_path)

    print("=== Isi CV (cv1.pdf) sebelum di preprocessing ===\n")
    print(resume_text[:500])

    recommendations = get_recommendations(resume_text)

    print("\n=== Top Job Recommendations ===")
    print(recommendations.to_string(index=False))