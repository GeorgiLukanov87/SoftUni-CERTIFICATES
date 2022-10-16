company_name = input()
count_tickets_normal = int(input())
count_tickets_kids = int(input())
price_ticket_normal = float(input())
tax_service = float(input())
price_ticket_kids = price_ticket_normal * 0.30
price_ticket_normal_tax_service = price_ticket_normal + tax_service
price_ticket_kids_tax_service = price_ticket_kids + tax_service
total_sum = (count_tickets_kids * price_ticket_kids_tax_service) + \
            (count_tickets_normal * price_ticket_normal_tax_service)
total_sum *= 0.20
print(f"The profit of your agency from {company_name} tickets is {total_sum:.2f} lv.")