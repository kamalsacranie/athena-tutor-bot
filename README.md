# Athena Job Scraper

I joined this tutoring company called Athena Tutors where they post 'jobs' where you can ask them to put you forward to the client.
During the first few days I was wondering why I wasn't gettin any news about new listings/jobs. I logged on and sure enough there were
plenty listings there. I knew this is the type of thing I'd forget to check and lose out on some good clients so I decided to write this
little Python app. The gist of the app is:

1. We unfortunately have to use Selenium in a headless browser to login and pull the job listings
2. We then use bs4 to parse listings and format them into a list of dictionaries
3. We then pickle that object for future reference
4. We unpickle the object from last time the script was run and compare the two list of dictionaries
5. We send the new listings to Yagmail where it sends me an email to notify me of new jobs