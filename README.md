# Download Invoices

It's just a simple bot that I wanted to use to download invoices from a merchant that uses [Billing Portal](https://www.billingportal.com/) to send and store them. It felt a little tedius to click through the website, so I used this as an oppurtunity to learn how to make a **web scraping bot** using **Selenium**. 

Unfortunately, it didn't work out.

This bot would have retrieved a login link from Billing Portal, and then use that link to login and download all the invoices from 2022. 

I wasn't able to properly retrieve a login link from my email. And even if I did, the website is secure enough to prevent bots from accessing it. 

## Update

Actually, I gave up on this program too early. I thought the website's security prevented me from working any further on this program, but adding a minor adjustment to my code fixed the whole thing:

### Before: 

`driver.get(os.getenv('LINK')))`

### After:

`driver.get(str(os.getenv('LINK')))` 

Regardless, I spent too much time on this bot than if I were to manually download the invoices. Therefore, I'll work on better projects in the meantime. 