phishing_keywords = [
"urgent",
"password reset",
"verify your account",
"click here",
"login immediately",
"confirm credentials"
]

emails = [
"Your password expires today. Click here immediately to reset.",
"Verify your banking credentials immediately.",
"Reminder about our meeting tomorrow."
]

for email in emails:

email_lower = email.lower()
