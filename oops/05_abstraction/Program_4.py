from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

    def log_notification(self, message):
        print(f"Notification Logged: {message}")

class EmailNotification(Notification):
    def send(self, message):
        super().log_notification(message)
        print(f"Email Sent: {message}")

class SMSNotification(Notification):
    def send(self, message):
        super().log_notification(message)
        print(f"SMS Sent: {message}")

email = EmailNotification()
sms   = SMSNotification()

email.send("Welcome")
sms.send("Hello")