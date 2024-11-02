<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# Unclock 🕑
**The Project uses Groq AI which is free and open source. Not to be confused with Grok developed by X.ai**

## Basic Details
### Team Name: Redbone


### Team Members
- Team Lead: Navaneeth V. Sankar - College of Engineering, Trivandrum
- Member 2: Aithel Christo - College of Engineering, Trivandrum

### Project Description
Unclock is a versatile clock that performs various unfunctions. It has a world clock, a stopwatch, a timer and an alarm all with a twist ;)

### The Problem (that doesn't exist)
The hegemony of the standardized clock system. The entrapment of SI units, fixed locations and linear time progression must be overcome.

### The Solution (that nobody asked for)
1. World Clock - Ever wanted time from another place but felt too lazy to pick the place? We've got you covered. You just have to click Add Time. We'll pull random locations from around the world and give you the time from there.
2. Stopwatch - A standard stopwatch. Except the units aren't standard. The time is displayed in handpicked(AI Generated on every restart) units of time.
3. Timer - Runs just like any other timer. Except the real time weather from your locality slows or speeds it down to match your vibe. Rainy weather ensures slower clock speed while hotter weather makes it faster.
4. Alarm - Plays an alarm sound as loud as possible. We've abstracted away the time setting for you. It plays if and when you click the button. No more snooze or stop buttons. Or any other buttons as a matter of fact

## Technical Details
### Technologies/Components Used
For Software:
- Python, JS, HTML, CSS
- Flask
- flask, pytz, groq, timezonefinder
- Open Weather Map, Groq AI


### Implementation
The app has been implemented using the flask python framework. The home page runs using app.py and is structured in index.html. The other features have been implemented as linked pages defined in the features folder. 
The world clock randomly picks a location, finds the nearest timezone and displays the time.
The units.py file generates a new unit of time using Groq AI everytime the stopwatch is reset. The stopwatch runs by dividing the elapsed time by the new unit of time.
The timer takes in the device location, obtains the last updated weather as shown in Open Weather Map. It then calculates a dilation factor based on the various prevailing weather conditions. This dilation factor directly slows or speeds up the timer based on the weather.
The alarm simply uses a JavaScript trigger to play an alarm noise

# Installation
```bash
pip install Flask groq pytz timezonefinder dotenv requests
```

# Run
## Setup

1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Fill in the actual values in `.env`.
3. Or obtain a groq API key of your own and set it up in units.py as shown. It is free and takes very little time.
   ```bash
   os.environ["GROQ_API_KEY"] = "your_key_here"
   ```
## Run
python app.py (Open in localhost or port)

# Screenshots
![image](https://github.com/user-attachments/assets/eebd5f2a-94e4-481f-b5ac-09997da8a193)
* home page

![image](https://github.com/user-attachments/assets/1db3adcc-b8ae-41d5-8716-7f85ef7079d2)
* world clock

![image](https://github.com/user-attachments/assets/bb0d4891-0253-4abc-9a06-fda85c46e35e)
* stopwatch

![image](https://github.com/user-attachments/assets/bf4c1f58-4f9d-4f9b-a9d1-d17440850709)
* VS CODE shot for proffesionalism


### Project Demo
# Video
[https://drive.google.com/file/d/1ICAN2cbRFHUA158VIkr-dBHVGW8HK9-z/view?usp=sharing]
The video displays all the features of the unclock app, except for alarm which requires sound.


## Team Contributions
- Navaneeth V. Sankar: Stopwatch, Design, AI
- Aithel Christo: World Clock, Timer, Flask Setup, Timezone and Weather integration

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)


