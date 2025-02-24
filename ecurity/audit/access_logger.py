class AccessLogger:
    def log_access(self, user: str, action: str) -> None:
        print(f"User {user} performed {action}.")
