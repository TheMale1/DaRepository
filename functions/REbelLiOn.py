"""keep track of ticket sales a cinema
"""

# This function runs the main program and coordinates calls to other functions
def main_routine():
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0

    ticket_wanted = input("Do you want to sell a ticket? (Y/N): ").upper()
    while ticket_wanted != "N":
        ticket = sell_ticket()

        # get the number of tickets wanted in the category chosen
        num_ticket = int(input("How many tickets do you want: "))
        confirm = input(f"Confirm purchase of {num_ticket} type {ticket} "
                        f"ticket(s)? (Y/N): ").upper()
        if confirm == "Y":
            price = num_ticket * float(get_price(ticket))
            total_sales += num_ticket
            if ticket == "A":
                adult_tickets += num_ticket
            elif ticket =="S":
                student_tickets += num_ticket
            elif ticket == "C":
                child_tickets += num_ticket
            else:
                gift_tickets += num_ticket

                ticket_wanted = input("\nDo you want to sell "
                                      "another ticket? (Y/N): ").upper()

                print("========================================")
                print(f"The total number of tickets sold today was {tickets_sold}\n"
                      f"This was made up of: \n"
                      f"\t{adult_tickets} for adults; and \n"
                      f"\t{student_tickets} for students; and \n"
                      f"\t{child_tickets} for children; and \n"
                      f"\t{gift_tickets} gift vouchers \n")
                print(f"The total sales for today came to ${total_sales:.2f}")
                print("========================================")

# Get category of ticket the purchaser wants
def sell_ticket():
    ticket_type_ = input("What kind of ticket do you want: \n"
                         "\tA for Adult, or\n"
                         "\tS for Student, or\n"
                         "\tC for Child, or\n"
                         "\tG for Gift voucher\n"
                         ">> ").upper()  # uppercase to minimise input errors
    return ticket_type_


# Get price for each ticket in the category chosen
def get_price(type_):
    prices = [["A", 12.5], ["S", 9], ["C", 7], ["G", 0]]
    for price in prices :
        if price [0] ==type_:
            return price[1]


# Main routine
print("**************** Fanfare Movies - ticketing system ****************\n")
main_routine()





