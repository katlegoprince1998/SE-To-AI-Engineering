class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        return f"Username: {self.username}, Email: {self.email}"

    def update_email(self, new_email):
        self.email = new_email
        return f"Email updated to: {self.email}"
    
    def __str__(self):
        return f"User({self.username}, {self.email})"
    
# Example usage:
if __name__ == "__main__":
    User = User("john_doe", "john@example.com")

    print(User.display_info())

    print(User.update_email("john_new@example.com"))

    print(User)