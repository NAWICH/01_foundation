# 🛠️ Automated File Organizer (Day 6)

A robust Python automation script designed to declutter directories by intelligently sorting files into categorized subfolders based on their extensions.

## 🚀 Overview
This project marks the final day of my **Python Systems Foundation** week. It solves the common problem of a "messy" Downloads or Desktop folder by implementing a decision engine that handles file categorization, directory management, and secure file transfers.

## ✨ Key Features
* **Extension Mapping:** Uses a dictionary-based "Brain" to categorize files into Images, Docs, Archives, and Scripts.
* **Dynamic Directory Creation:** Automatically detects if a category folder exists and creates it on-the-fly using `os.makedirs`.
* **Safe File Operations:** Utilizes the `shutil` module for high-level file movements, ensuring compatibility across different file systems.
* **Collision & Misc Handling:** Includes logic to handle unknown file types (moved to `Others`) and prevents script crashes.
* **Batch Processing Report:** Generates a final summary in the terminal showing exactly how many files were organized.

## 🛠️ Technical Skills Demonstrated
* **High-Level File I/O:** Using `shutil.move` for reliable data relocation.
* **Path Surgery:** Advanced use of `os.path.splitext` and `os.path.join`.
* **Data Aggregation:** Using dictionary comprehensions and counters to track automation results.
* **Edge Case Management:** Handling case-sensitivity (e.g., .JPG vs .jpg) and directory-skipping logic.

## 📦 How to Use
1. Run the script:
   ```bash
   python organizer.py