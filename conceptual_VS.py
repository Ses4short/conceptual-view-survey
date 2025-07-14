D:\OneDrive - Prince of Songkla University\เอกสาร\conceptual_VS.py

"C:\Users\sherif.s>pip install streamlit
'pip' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\sherif.s>

#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import datetime

# --- Page Config ---
st.set_page_config(page_title="Conceptual View Survey", layout="centered")

st.title("📊 User Survey on Explainability of Boosting Models")
st.markdown("""
This short survey aims to understand how users interpret explanations generated from two types of conceptual views derived from Gradient Boosting and XGBoost models.

📌 **Note:** Both explanations lead to the same model prediction. Your task is to judge how understandable the explanation itself is — not the predicted outcome.

Your responses are anonymous and will only be used for research purposes.
""")

st.markdown("---")

# --- View 1: Leaf View Explanation ---
st.header("🟩 Explanation A: Leaf View (XGBoost)")
st.markdown("""
> The model classifies a car as **acceptable** because:
>
> - The **safety rating** is *low*
> - The **number of doors** is *2*
> - The **price** is *very high*
""")

st.subheader("How understandable is this explanation?")
q1 = st.radio("1. I can understand the reasoning behind the model's decision.", 
              ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"], key="q1")

q2 = st.radio("2. The explanation is clear and concise.", 
              ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"], key="q2")

st.markdown("---")

# --- View 2: Tree Predicate View Explanation ---
st.header("🌳 Explanation B: Tree Predicate View (Gradient Boosting)")
st.markdown("""
> The model classifies a car as **acceptable** because:
>
> - The **maintenance cost** is *low*
> - The **number of persons** it can carry is *more than 4*
> - The **trunk size** is *large*
> - The **price** is *medium*
""")

st.subheader("How understandable is this explanation?")
q3 = st.radio("3. I can understand the reasoning behind the model's decision.", 
              ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"], key="q3")

q4 = st.radio("4. The explanation is clear and concise.", 
              ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"], key="q4")

st.markdown("---")

# --- Comparative Preference ---
st.subheader("Overall Preference")
q5 = st.radio("5. Which explanation did you find more interpretable?", 
              ["Explanation A (Leaf View)", "Explanation B (Tree Predicate View)", "Both equally", "Neither"])

st.markdown("---")

# --- Optional Feedback ---
comments = st.text_area("Any comments or suggestions?", placeholder="Write here (optional)...")

# --- Consent and Submit ---
consent = st.checkbox("I understand and agree to participate in this anonymous survey for research purposes.")

if consent and st.button("Submit My Response"):
    response = {
        "timestamp": datetime.datetime.now(),
        "q1_leaf_understand": q1,
        "q2_leaf_clear": q2,
        "q3_tree_understand": q3,
        "q4_tree_clear": q4,
        "q5_preference": q5,
        "comments": comments
    }

    # Save to CSV (append)
    df = pd.DataFrame([response])
    try:
        df.to_csv("survey_responses.csv", mode='a', index=False, header=not pd.io.common.file_exists("survey_responses.csv"))
        st.success("✅ Thank you! Your response has been recorded.")
    except Exception as e:
        st.error(f"⚠️ Failed to save your response: {e}")
elif not consent:
    st.warning("Please check the box to give your consent before submitting.")

