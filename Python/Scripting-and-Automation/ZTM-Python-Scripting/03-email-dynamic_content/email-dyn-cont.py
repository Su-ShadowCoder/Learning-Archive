import smtplib
from email.message import EmailMessage
#
from string import Template
from pathlib import Path 
#

#
html = Template(Path('index.html').read_text())
#

email = EmailMessage()
email['from'] = 'sudarshen kandasamy'
email['to'] = 'warlordwarlordwarlord007@gmail.com'
email['subject'] = "You won 5,000,000 euro!"

#
email.set_content(html.substitute({'name': 'Tintin'}), 'html')
#

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('warlordwarlordwarlord007@gmail.com', 'nrtv iarr uwop zdwq')
    smtp.send_message(email)
    print('Job is done boss!!')


