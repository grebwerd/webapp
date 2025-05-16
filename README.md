# Web App — Project Plan

### Let's work on this in phases to make sure we have a clear understand of each phase, what it means and why it's important. Try to keep each phase of work in a single PR. When we getto some of the more complicated phases, we can break them up into multiple PRs.

### Start by creating your branch and work on Phase 1 by creating a docs directory, and storing this information in .md files inside that directory. Once that's complete you can put up a PR and we can discuss!



## 📅 Phase 1: Define the Product

### Investment Portfolio Simulator
#### Description:

The application will allow the user to create a stock portfolio comprised of stocks found on large exchanges
(NYSE, NASDAQ, FTSE...etc) and well known cryptocurrencies.

#### Core functionality:

The application will be REST based and allow the user to perform crud operations on their investment portfolio.

A core feature will be to compare the user's portfolio performance against well known bench indices (S&P 500, DJIA, Nasdaq composite) for a
specified range of time.

#### Stretch goals:

Create a notification to be sent to the user when a desired stock/crypto hits a specified price.

---

## 📈 Phase 2: Design the Architecture

4. Diagram the high-level system (frontend, backend, database, API). (Use draw.io)
5. Choose technologies for each part of the stack.

---

## 📊 Phase 3: Design the Database

6. List the types of data the app will store.
7. Design a normalized schema for stock data and features.
8. Pick a database (SQL preferred) and set it up locally using your tech stack choices.

---

## 🔹 Phase 4: Pick & Integrate a Stock API

9. Research available stock APIs and their free tiers.
10. Choose an API and read its documentation.
11. Write out the endpoints and data you’ll need.
12. Decide how often you’ll sync or fetch new data.

---

## 🛠️ Phase 5: Build the Backend

13. Set up a simple backend server.
14. Define the API routes you’ll expose to the frontend.
15. Add logic to pull stock data from the stock API.
16. Store retrieved data in your database.
17. Implement simple "buy signal" evaluation logic based on metrics.
18. Wriite tests to get tot 100% unit coverage.
---

## ⏰ Phase 6: Implement Scheduled Tasks

19. Set up a cron job or scheduled worker to run daily.
20. Automate fetching new stock data.
21. Store new recommendations in the database.

---

## 🖥 Phase 7: Build the Frontend

22. Design wireframes for the main screens (search, recommendations).
23. Choose a UI framework or CSS library.
24. Build a stock search page with result display.
25. Build a recommendations dashboard showing “buy” picks.
26. Add loading states, error states, and basic responsiveness.
27. Write tests to get to 100% unit coverage.
---

## 🌐 Phase 8: Deploy the App

28. Chances are, if we get to this point. We'll keep this all local. But if we get here with enough time left, and get approval to deploy, then we can take it from there.

---

## ⚡ Phase 9: Improve UX and Performance

29. Add loading spinners or skeletons for API responses.
30. Optimize database queries if needed.
31. Add pagination or limits to result sets.

---

## 🚀 Phase 10: Optional Stretch Goals

32. Add user accounts (auth system).
33. Let users save favorite stocks or set alerts.
34. Add a portfolio tracker with simulated buys.
35. Implement basic backtesting for your strategies.
36. Send daily/weekly recommendation emails.

