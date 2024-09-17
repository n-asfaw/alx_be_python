# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority and time sensitivity
match priority:
    case "high":
        message = f"'{task}' is a high priority task."
    case "medium":
        message = f"'{task}' is a medium priority task."
    case "low":
        message = f"'{task}' is a low priority task."
    case _:
        message = f"'{task}' has an unknown priority."

# Modify message if task is time-sensitive
if time_bound == "yes":
    message += " It requires immediate attention today!"
else:
    message += " Consider completing it when you have free time."

# Output the customized reminder
print(f"Reminder: {message}")

