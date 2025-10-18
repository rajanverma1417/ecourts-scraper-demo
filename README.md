
# 🧾 eCourts Scraper Demo

A simple **Python project** that simulates fetching eCourts case data and generating a fake cause list.  
This project was made as part of an **internship assignment** to demonstrate data validation, loops, and basic file handling in Python.

---

## 💻 How to Run

1. **Clone or Download** this repository:
   git clone https://github.com/rajanverma1417/ecourts-scraper-demo.git
   cd ecourts-scraper-demo

   
Run the Python script:

python "internship_project.py"

⚙️ Features
✅ Input validation for menu options

🧾 CNR (Case Number Record) format checking

💡 Fake case details & cause list generation (demo purpose)

💾 Stores results in case_result.json and cause_list.txt

🔁 Option to continue or exit smoothly

🧠 Requirements
Python 3.8+

Uses only built-in libraries (json, datetime, random)

No external installations required

📂 Files Created by Script
File Name	Description
case_result.json	Stores the fake case data result
cause_list.txt	Saves generated cause list text

🚀 Example Usage
When you run the script:

You’ll see a small menu:

1. Check case listing

2. Download today's cause list

Enter your choice → program validates it.

If you enter a fake CNR, it generates and saves fake data.

You can continue until you type “no”.

🧩 Future Improvements
Replace demo data with real eCourts scraping (with proper permissions).

Add command-line arguments for automated runs.

Add logging and better error handling.

✨ Author
Rajan Varma
📧 rajanverma1417@gmail.com

📜 License
You can use or modify this project freely for learning purposes.
Suggested: MIT License

🌟 Star this repo if you found it helpful!
