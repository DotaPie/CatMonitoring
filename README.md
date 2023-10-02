# CatMonitoring  
This project records 2 USB web cams (can be 1-4) on motion and then upload them to your google drive and delete them afterwards. Will work on most of the linux platforms.   
Recording is handled by linux motion library.  
Video uploading is handled by python script (using google API).  
At this point, linux host computer must have GUI enabled with any rowser installed, so script can redirect to browser for authentication.  

# Installation guide  
## Allow google API on your account and generate credentials.json:  
	--> just watch and follow https://www.youtube.com/watch?v=fkWM7A-MxR0  
  
## Python script install:  
	**CMD:** sudo apt update && sudo apt upgrade -y  
	**CMD:** mkdir /home/$USER/CatMonitoring  
	--> copy all provided files there + also obtained credentials.json from google API  
	--> check paths in the python script in the top of the script  
	**CMD:** mkdir /home/$USER/CatMonitoring/CatMonitoringEnv  
	**CMD:** python3 -m venv /home/$USER/CatMonitoring/CatMonitoringEnv   
	**CMD:** python3 -m pip install --upgrade pip  
	**CMD:** python3 -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib  
  
## Motion install:  
	**CMD:** sudo apt install motion  
	**CMD:** sudo rm -rf /etc/motion/*  
	**CMD:** sudo cp /home/$USER/CatMonitoring/MotionConfs/* /etc/motion  
	**CMD:** mkdir /home/$USER/CatMonitoring/Videos  
	**CMD:** sudo chmod 777 /home/$USER/CatMonitoring/Videos  
	--> check paths and other settings in /etc/motion/ conf files  
  
## Run motion (in separate console window):  
	**CMD**: sudo motion  
  
## Run python script (in separate console window):  
	**CMD**: /home/$USER/CatMonitoring/CatMonitoringEnv/bin  
	**CMD**: source ./activate  
	**CMD**: python3 /home/$USER/CatMonitoring/VideosToDriveSync.py  
	--> authorize via web browser to your google account (needed only once)  
	



