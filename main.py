

def log_ticket():
    ticketID = 1
    print("||You have selected to log a ticket||")
    print(f"||Ticket number {ticketID} has been created||")
    issue = str(input("Please enter the description of the issue you would like to log: "))
    typesOfIssues  = ["Hardware", "Software", "Network", "Security", "User Accounts", "Email", "Data & Storage", "Performance", "Software Testing", "Automation"]
    for number , category in enumerate(typesOfIssues,1):
        print(f"{number}: {category}")
    categorySelection = int(input("Please enter the category you would like to use: "))
    categorySelection = categorySelection - 1
    print(f"Okay your issue has been logged as a {typesOfIssues[categorySelection]} error ")
    ticket = {
        "ticketID": ticketID,
        "issue": issue,
        "category": categorySelection,
        "status": True
    }
    print(ticket)

if __name__ == '__main__':
    log_ticket()


