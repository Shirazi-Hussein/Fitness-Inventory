https://www.fitnessinventory.info/

# How does it work?
There are 12 individual python scripts that scrape the products from 6 different fitness suppliers, 2 scripts for each one. 1 for the barbell items, the other for plate items.
Each file supports threading and uses BS4 alongside requests, or for websites like Rogue Fitness that places limits on bots, I've had to switch to an alternative that better 
mimicked a real user. Selenium was the next choice, but I soon found out that it didn't support threading, so I abandoned it. There's an overhead file called main.py that 
executes all 12 scripts and combines them into a single CSV file. Without threading, the process would take maybe 8 minutes. With threading, its around 45 seconds to a minute 30.

# How did you deploy it?
It's deployed via Flask, a micro-framework. I thought it was more suitable than Django given the simplicity of the project. It's currently hosted on Google Cloud Platform and 
the domain was pretty cheap on Google Domains. 
