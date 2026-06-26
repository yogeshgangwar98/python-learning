class EmailNotification:
    def send(self, message):
        print(f"Email Sent: {message}")

class SMSNotification:
    def send(self, message):
        print(f"SMS Sent: {message}")

class PushNotification:
    def send(self, message):
        print(f"Push Notification Sent: {message}")

notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for notification in notifications:
    notification.send("Welcome")
