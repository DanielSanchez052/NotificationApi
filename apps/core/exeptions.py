class NotificationException(Exception):
    def __init__(self, message="Error Has Ocurred During Execute notification", *args: object) -> None:
        self.message = message
        super().__init__(*args)

    def __str__(self) -> str:
        return self.message
