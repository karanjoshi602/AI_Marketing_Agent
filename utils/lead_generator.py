import random

# ---------------- LEAD SCORING ---------------- #

def calculate_score(row):

    score = 0

    if row["Interest_Level"] == "High":
        score += 50

    elif row["Interest_Level"] == "Medium":
        score += 30

    else:
        score += 10

    if row["Company_Size"] >= 1000:
        score += 40

    elif row["Company_Size"] >= 500:
        score += 25

    else:
        score += 10

    return score


# ---------------- AI RECOMMENDATIONS ---------------- #

def generate_recommendations():

    recommendations = [
        "High conversion probability",
        "Strong enterprise potential",
        "Suitable for AI automation services",
        "Likely interested in cybersecurity solutions",
        "Potential long-term client"
    ]

    return random.choice(recommendations)