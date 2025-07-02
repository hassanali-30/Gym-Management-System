# gym_system.py

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class Member(User):
    def __init__(self, username, age, goal):
        super().__init__(username, 'Member')
        self.age = age
        self.goal = goal
        self.schedule = None

    def view_profile(self):
        print(f"\n--- Member Profile ---")
        print(f"Username: {self.username}")
        print(f"Age: {self.age}")
        print(f"Fitness Goal: {self.goal}")
        print(f"Workout Schedule: {self.schedule if self.schedule else 'Not assigned'}")

class Trainer(User):
    def __init__(self, username):
        super().__init__(username, 'Trainer')
        self.assigned_members = []

    def view_members(self):
        print(f"\nTrainer: {self.username}'s Members")
        if not self.assigned_members:
            print("No members assigned.")
        for m in self.assigned_members:
            print(f"- {m.username} | Goal: {m.goal}")

    def assign_schedule(self, member, schedule):
        member.schedule = schedule
        print(f"Assigned schedule to {member.username}: {schedule}")

class Admin(User):
    def __init__(self, username):
        super().__init__(username, 'Admin')

    def add_trainer(self, trainers, username):
        trainer = Trainer(username)
        trainers.append(trainer)
        print(f"Trainer {username} added.")

    def add_member(self, members, username, age, goal):
        member = Member(username, age, goal)
        members.append(member)
        print(f"Member {username} added.")

    def view_all(self, trainers, members):
        print("\n--- All Trainers ---")
        for t in trainers:
            print(f"- {t.username}")
        print("\n--- All Members ---")
        for m in members:
            print(f"- {m.username} | Age: {m.age} | Goal: {m.goal}")

# --- Sample Usage ---
def main():
    admin = Admin("admin")
    trainers = []
    members = []

    while True:
        print("\n--- Gym Management System ---")
        print("1. Admin Panel")
        print("2. Trainer Panel")
        print("3. Member Panel")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("\n[Admin Panel]")
            print("1. Add Trainer")
            print("2. Add Member")
            print("3. View All Users")
            sub = input("Enter option: ")
            if sub == "1":
                uname = input("Enter trainer username: ")
                admin.add_trainer(trainers, uname)
            elif sub == "2":
                uname = input("Enter member username: ")
                age = int(input("Enter age: "))
                goal = input("Enter fitness goal: ")
                admin.add_member(members, uname, age, goal)
            elif sub == "3":
                admin.view_all(trainers, members)

        elif choice == "2":
            tname = input("Enter trainer username: ")
            trainer = next((t for t in trainers if t.username == tname), None)
            if trainer:
                print(f"\nWelcome {trainer.username}")
                print("1. View Assigned Members")
                print("2. Assign Workout Schedule")
                sub = input("Enter option: ")
                if sub == "1":
                    trainer.view_members()
                elif sub == "2":
                    mname = input("Enter member username: ")
                    member = next((m for m in members if m.username == mname), None)
                    if member:
                        schedule = input("Enter workout schedule: ")
                        trainer.assign_schedule(member, schedule)
                        if member not in trainer.assigned_members:
                            trainer.assigned_members.append(member)
                    else:
                        print("Member not found.")
            else:
                print("Trainer not found.")

        elif choice == "3":
            mname = input("Enter member username: ")
            member = next((m for m in members if m.username == mname), None)
            if member:
                member.view_profile()
            else:
                print("Member not found.")

        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
