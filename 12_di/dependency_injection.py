from abc import ABC, abstractmethod


# АТД MessageService
class MessageService(ABC):
    @abstractmethod
    def send_message(self, message: str, recipient: str): ...


# Реализация сервиса отправки Email
class EmailService(MessageService):

    def send_message(self, message: str, recipient: str):
        print(f"Email sent to {recipient} with message: {message}")


# Реализация сервиса отправки SMS
class SmsService(MessageService):

    def send_message(self, message: str, recipient: str):
        print(f"SMS sent to {recipient} with message: {message}")


# Класс уведомлений, использующий Dependency Injection
class NotificationService:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service

    def notify_user(self, message: str, user: str):
        self.message_service.send_message(message, user)


if __name__ == "__main__":
    # Внедрение EmailService
    email_service = EmailService()
    notification_service = NotificationService(email_service)
    notification_service.notify_user("Hello, User!", "user@example.com")

    # Внедрение SmsService
    sms_service = SmsService()
    notification_service = NotificationService(sms_service)
    notification_service.notify_user("Hello, User!", "123-456-7890")
