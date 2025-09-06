# Ubuntu Requests – Image Fetcher

A **Python script** that fetches images from the web, saves them locally, and handles errors gracefully — inspired by the Ubuntu philosophy: *“I am because we are.”*

---

## ✨ Features

* Prompts the user for an image URL.
* Creates a directory called **`Fetched_Images`** (if it doesn’t exist).
* Downloads and saves the image with the correct filename.
* Handles errors gracefully (invalid URL, network issues, etc.).
* Prints clear success and failure messages.

---

## 📦 Technologies Used

* Python 3
* [`requests`](https://docs.python-requests.org/) → to fetch the image
* `os` → to create directories and manage files
* `urllib.parse` → to extract filenames from URLs

---

## 🚀 How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/Ubuntu_Requests.git
   cd Ubuntu_Requests
   ```

2. **Install dependencies**

   ```bash
   pip install requests
   ```

3. **Run the script**

   ```bash
   python fetch_image.py
   ```

4. **Enter an image URL** when prompted, e.g.:

   ```
   https://picsum.photos/400/300
   ```

---

## 📂 Example Output

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.
```

---

## 🌍 Ubuntu Principles in Action

* **Community**: Connects to the wider web and shares resources.
* **Respect**: Handles errors gracefully without crashing.
* **Sharing**: Organizes downloaded images for later use.
* **Practicality**: Provides a simple, real-world utility.

