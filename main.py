
class Ticket():
    def __init__(self, ticketid, category, description , priority,status):
        self.ticketid = ticketid
        self.category = category
        self.description = description
        self.priority = priority
        self.status = "Open"
    def closeTicket(self):
        self.status = "Closed"
    def displayTicket(self):
        print(self.ticketid)
        print(self.category)
        print(self.description)
        print(self.priority)
        print(self.status)
    def update_priority(self, new_priority):
        self.priority = new_priority
        print('The priority has now been updated')


def log_ticket():
    ticketID = 1
    print("||You have selected to log a ticket||")
    print(f"||Ticket number {ticketID} has been created||")
    issue = str(input("Please enter the description of the issue you would like to log: "))

    priority =  ["Low", "Medium", "High" , "Critical"]
    ticketPriority = priority[1]

    typesOfIssues  = ["Hardware", "Software", "Network", "Security", "User Accounts", "Email", "Data & Storage", "Performance", "Software Testing", "Automation"]
    for number , category in enumerate(typesOfIssues,1):
        print(f"{number}: {category}")
    print("")
    categorySelection = int(input("Please enter the category you would like to use: "))
    categorySelection = categorySelection - 1
    print("")
    print(f"Okay your issue has been logged as a {typesOfIssues[categorySelection]} error ")

    ticket = Ticket(
        ticketID,
        typesOfIssues[categorySelection],
        issue,
        ticketPriority,
        True
    )
    return ticket
if __name__ == '__main__':
    ticket = log_ticket()
    updatePriority = str(input("Please enter the priority you would like to update: "))
    ticket.update_priority(updatePriority)
