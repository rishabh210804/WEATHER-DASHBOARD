# WEATHER-DASHBOARD
COMPANY: CODTECH IT SOLUTIONS

NAME: RISHABH CHOUHAN

INTERN ID: COD123

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

 Internship Task 1: Weather Data Visualization Using API

Objective:

The objective of this task was to develop a complete Python-based application that fetches real-time weather data from a public API, processes and stores it in a structured format, and then visualizes the data using standard Python visualization libraries. This task demonstrates a practical understanding of API integration, data processing using Pandas, and visual representation using Matplotlib and Seaborn. The goal was to create a mini weather dashboard that presents key weather metrics for multiple cities, offering a simplified and informative view of weather conditions.

⸻

Tools & Technologies Used:
	•	Programming Language: Python 3
	•	API Source: OpenWeatherMap API
	•	Libraries:
	•	requests – for handling HTTP requests and API integration
	•	pandas – for organizing and analyzing data
	•	matplotlib – for basic plotting
	•	seaborn – for enhanced statistical visualization
	•	Platform: macOS (Terminal)
	•	Output Format: Bar plots and structured tabular data

⸻

🔧 Implementation Steps:

1. API Setup and Key Generation:

The first step was to register an account with OpenWeatherMap to obtain a free API key. This key allows access to real-time weather data through HTTP requests. The Current Weather API endpoint was selected, as it provides essential weather metrics such as temperature, humidity, and general weather condition (e.g., clear, cloudy, rainy).

2. Writing the Python Script:

A Python script was written to request data from the OpenWeatherMap API. The script included a list of selected Indian cities: Mumbai, Delhi, Bangalore, Chennai, and Kolkata. A for loop was used to fetch data for each city using the requests.get() function. The response, in JSON format, was parsed to extract temperature, humidity, and weather description.

3. Data Storage Using Pandas:

The extracted data for each city was organized in a dictionary and appended to a list. Once all the data was fetched, this list of dictionaries was converted into a Pandas DataFrame. This structured format made it easy to view and manipulate the data, and also served as the basis for generating visualizations.

4. Visualization with Matplotlib:

The first visualization was a basic bar chart showing the temperature of each city using Matplotlib. The plot included appropriate labels, a grid, and a title, making the information clear and easy to understand. This visualization helped compare temperature variations across cities.

5. Advanced Visualization with Seaborn:

The second visualization was created using Seaborn, a powerful Python visualization library built on top of Matplotlib. A bar plot was generated to display the humidity levels of the same cities. Seaborn’s styling options, like color palettes and layout control, helped present the data in a more professional and visually appealing way.

⸻

 Error Handling:

Basic error handling was implemented to manage failed API requests. If any city returned an unsuccessful status code, a warning message was printed, and the program continued fetching data for the remaining cities. This made the script more robust and production-ready.

⸻

Output and Results:
	•	A printed DataFrame showing city-wise temperature, humidity, and weather description.
	•	A Matplotlib-based bar chart of city-wise temperature (°C).
	•	A Seaborn-based bar chart of city-wise humidity (%).
	•	All outputs were generated dynamically based on real-time data fetched from the API.

⸻

 Files and Deliverables:
	•	weather_dashboard.py – complete Python script
	•	Screenshot(s) of the plots and output for submission
	•	API key was used securely and can be replaced for future use
	•	Optional: can be extended into a dashboard using Streamlit

⸻

Conclusion:

This task successfully demonstrated the complete workflow of a real-world data science mini-project: integrating with an external data source, performing data extraction and transformation, and using visualization to gain insights. It helped reinforce Python programming concepts, API handling, JSON parsing, and effective use of data analysis libraries. Moreover, it showcased the ability to translate raw data into meaningful visual stories, which is a crucial skill in data analytics and software development.

This task forms a foundational step towards more complex applications like dashboards, forecasting models, or integrating data from multiple APIs.


#OUTPUT

<img width="1792" alt="Image" src="https://github.com/user-attachments/assets/00ef5b2a-f483-4219-a14e-e104c463f835" />
<img width="1792" alt="Image" src="https://github.com/user-attachments/assets/313da8f6-88e4-4dd7-b1d3-d5116755a32e" />
<img width="1792" alt="Image" src="https://github.com/user-attachments/assets/df4ffd9e-0e4d-4f27-81de-200d099442cc" />
