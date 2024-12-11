import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define your SMTP email server details
SMTP_SERVER = 'SMTP.server.com'  # e.g., 'smtp.gmail.com, smtp.hostinger.com'
SMTP_PORT = 587  # Usually 587 for TLS
EMAIL_ADDRESS = 'Your_Email'
EMAIL_PASSWORD = 'Your_Password'

# Function to send an email
def send_email(recipient_email, recipient_name):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = "Unlock More Pipeline with Less Effort"

        # Email body with personalization
        body = f"""Hi {recipient_name},

In today's challenging market, where marketing budgets are tight and traditional demand generation tactics aren't delivering as they once did, SoundGTM offers a solution to help you do more with less.

We specialize in helping growth-stage SaaS companies like yours overcome:
- Pipeline challenges and customer budget constraints.
- Inefficient demand generation efforts.

With SoundGTM, you can:
- Generate qualified leads and revenue by accessing skilled referral partners.
- Seamlessly integrate with tools like HubSpot or Pipedrive.
- Only pay for results that meet your internal KPIs.

If you’re using platforms like Google Ads or LinkedIn Ads and can easily integrate JavaScript or Segment, getting started with SoundGTM is fast and impactful.

Are you ready to simplify your pipeline-building efforts?

https://app.soundgtm.com/c?atb_aff_id=4k9hkln&atb_offer_id=qyzckk&atb_lp_id=DKEC93

Best regards,
Krunalkumar Shah
        """

        msg.attach(MIMEText(body, 'plain'))

        # Connect to the server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Email sent to {recipient_name} at {recipient_email}")

    except Exception as e:
        print(f"Failed to send email to {recipient_name} at {recipient_email}: {e}")

# Read the CSV file and send emails
def send_emails_from_csv(csv_file_path):
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['First Name']
                email = row['Email']
                send_email(email, name)

    except FileNotFoundError:
        print(f"The file {csv_file_path} was not found.")
    except KeyError as e:
        print(f"Missing column in CSV file: {e}")

# Run the script
if __name__ == "__main__":
    csv_file_path = 'Emails.csv'  # Path to your CSV file
    send_emails_from_csv(csv_file_path)
