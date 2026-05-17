# 🏷️ Online Auction System

A simple Online Auction System where users can enter their name and bid amount. The owner can view all submitted bids sorted in ascending order, making it easy to select the highest or lowest bidder for contracts or auctions.

Built using Python for the backend and HTML/CSS for the frontend.

---

## 🚀 Features

- Users can submit:
  - Name
  - Bid Amount
- Displays all bids in sorted order
- Easy contract selection process
- Simple and user-friendly interface
- Beginner-friendly project

---

## 🛠️ Technologies Used

- Python
- HTML
- CSS

---

## 📂 Project Structure

```bash
onlineauctionsystem/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## ▶️ How It Works

1. Users enter their:
   - Name
   - Bid Amount

2. The system stores all bids.

3. The owner can view:
   - Lowest bid
   - Highest bid
   - Sorted list of all bids

This helps in selecting the best contract bidder easily.

---

## 💻 Example Output

```bash
Enter Your Name: Sai
Enter Your Bid Amount: 5000

Enter Your Name: Rahul
Enter Your Bid Amount: 3000

Enter Your Name: Kiran
Enter Your Bid Amount: 7000
```

### Sorted Bids

```bash
Rahul - ₹3000
Sai - ₹5000
Kiran - ₹7000
```

---

## 📜 Python Example Code

```python
bids = {}

while True:
    name = input("Enter Your Name: ")
    bid = int(input("Enter Your Bid Amount: "))

    bids[name] = bid

    more = input("Are there more bidders? yes/no: ")

    if more == "no":
        break

sorted_bids = sorted(bids.items(), key=lambda x: x[1])

print("\nSorted Bids:")

for bidder, amount in sorted_bids:
    print(f"{bidder} - ₹{amount}")
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/onlineauctionsystem.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd onlineauctionsystem
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

---

## 📌 Requirements

Example `requirements.txt`

```txt
Flask
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

- Python Dictionaries
- Sorting Data
- User Input Handling
- Flask Basics
- Frontend and Backend Integration
- HTML/CSS Design

---

## 🌟 Future Improvements

- Add database support
- Add login and authentication
- Add real-time bidding
- Add bid timer functionality
- Deploy online using Render

---

## 👨‍💻 Author

Created by Venkata Sai
