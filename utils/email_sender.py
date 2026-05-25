# ---------------- BULK EMAIL GENERATOR ---------------- #

def generate_bulk_email(row):

    subject = f"AI Solutions for {row['Company']}"

    email = f"""
To: {row['Email']}

Subject: {subject}

Dear {row['Name']},

We are reaching out to organizations in the
{row['Industry']} sector to introduce our
AI-powered automation and security solutions.

Our systems help businesses improve:
- operational efficiency
- customer intelligence
- cybersecurity
- digital transformation

We believe {row['Company']}
would be an excellent strategic partner.

Regards,
AI Marketing Team
    """

    return email