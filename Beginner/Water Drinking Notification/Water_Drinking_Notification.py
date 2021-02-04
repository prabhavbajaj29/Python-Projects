import time
from plyer import notification

if __name__=="__main__":
	while True:	
		notification.notify(
			title="Please Drink Water",
			message="Drinking Water keeps your body fit",
			app_icon="C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Notification\\icon.ico",
			timeout=10
        )
		time.sleep(15)