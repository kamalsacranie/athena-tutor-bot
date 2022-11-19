import yagmail

from constants import (
    gmail_username,
    gmail_password,
    email_receiver,
)


def send_update_email(new_jobs):

    # Pretty bloody simple, Generate some email contents etc.
    yagmail.register(gmail_username, gmail_password)
    yag = yagmail.SMTP(gmail_username)
    contents = _generate_email(new_jobs)
    yag.send(email_receiver, subject="New Athena Jobs", contents=contents)


def _generate_email(new_jobs):
    email_body = "<h1>New Athena Jobs</h1>"
    for i, job in enumerate(new_jobs):
        # Python f-strings save the day
        email_body += f"""
<div>
    <h2 style="display: inline; padding: 0 15px">
        { i+1 }. <a href="{job['link']}">{job['title']}</a>
    </h2>
    <li>
        <ul>Job rate per hour: {job['rate']}</ul>
        <ul>{job['synopsis']}</ul>
        <ul>Date added: {job['created_at']}</ul>
    </li>
</div>"""
    return email_body
