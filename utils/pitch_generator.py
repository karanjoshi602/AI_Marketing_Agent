# ---------------- AI PITCH GENERATOR ---------------- #

def generate_pitch(selected_row):

    pitch = f"""
Dear {selected_row['Name']},

Greetings from AI Marketing Solutions.

We analyzed your organization,
{selected_row['Company']},
and identified strong opportunities for
digital transformation and AI-driven automation.

Our solutions are specifically designed for the
{selected_row['Industry']} industry and can help improve:

• Operational efficiency
• Security infrastructure
• AI automation workflows
• Business intelligence systems

We would love to discuss how our AI-powered
services can support your business growth.

Regards,
AI Marketing Team
    """

    return pitch