Weather Data Management System
A Python-based utility that interfaces with the Open-Meteo API to fetch, process, and store real-time weather data for specific cities in Nepal. This project demonstrates API integration, environment variable management, and local data persistence.
🚀 Features

    Config-Driven: Cities and coordinates are managed via a central config.json.

    Human-Readable Data: Automatically converts WMO weather codes (e.g., Code 3) into descriptive text (e.g., "Overcast").

    Security: Uses .env files to manage API endpoints and sensitive keys.

    Data Persistence: Saves weather snapshots into unique JSON files named by city for easy data tracking.

    Robust Networking: Implements caching and retry logic to handle unstable internet connections.

🛠️ Tech Stack

    Language: Python 3.x

    API: Open-Meteo

    Libraries: * openmeteo-requests for API communication.

        python-dotenv for environment variable management.

        requests-cache & retry-requests for optimized networking.

        pandas for potential data manipulation.

📋 Prerequisites

Before running the script, ensure you have the following files in your directory:

    .env: Containing the base API URL.
    Code snippet

    url=https://api.open-meteo.com/v1/forecast

    day_9/config.json: Containing your city coordinates and requested weather variables.

🔧 Installation & Setup

    Clone the repository (or navigate to your project folder).

    Install dependencies:
    Bash

    pip install openmeteo-requests requests-cache retry-requests python-dotenv pandas

    Run the application:
    Bash

    python weather_manager.py

📊 How it Works

    Configuration: The script reads config.json to identify which cities are available and what metrics (temperature, humidity, etc.) to fetch.

    API Call: It sends a request to Open-Meteo using the latitude/longitude mapped to your choice.

    Processing: The system extracts raw numerical data and converts weather codes into user-friendly descriptions.

    Storage: A final report is generated and saved as {city_name}_data.json.

📝 Example Output
JSON
{
    "timestamp": "2026-01-29 23:15:00",
    "city": "kathmandu",
    "temperature_2m": "12.5°C",
    "relative_humidity_2m": "65%",
    "conditions": "Partly cloudy"
}