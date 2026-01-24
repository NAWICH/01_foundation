# 📂 Directory Health Scanner (Day 5)

A Python-based system utility designed for **Arch Linux** (or any Unix-based system) to analyze directory storage, categorize file sizes, and identify "space-hogs" in the file system.

## 🚀 Overview
As part of my **AgenticAiLabs AI Engineering Roadmap**, this project focuses on **System-Level Programming**. It demonstrates the ability to interact with the Operating System (OS), handle file metadata, and process data collections to generate meaningful reports.

## ✨ Key Features
* **Path Validation:** Checks if the user-provided directory exists before scanning.
* **Recursive Analysis:** Loops through directory contents using the `os` module.
* **Intelligent Metadata Extraction:** Retrieves file sizes in bytes and performs accurate mathematical conversions to MegaBytes (MB).
* **Automated Ranking:** Utilizes `lambda` sorting to identify and display the top 3 largest files found in the path.
* **Robust Error Handling:** Distinguishes between files and sub-directories to prevent scan crashes.

## 🛠️ Technical Skills Demonstrated
* **File System Operations:** `os.path`, `os.listdir`, and `os.path.join`.
* **Data Structures:** Implementation of dictionaries to map filenames to their respective sizes.
* **Functional Logic:** Use of the `sorted()` function with custom `lambda` keys for data ranking.
* **Formatting:** Clean CLI output using Python f-strings with 2-decimal precision.

## 📦 How to Use
1. Clone the repository.
2. Run the script:
   ```bash
   python scanner.py