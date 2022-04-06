# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
# wb = xl.load_workbook('transactions.xlsx')
# sheet = wb['Sheet1']
#
# def bla():
#     for row in range(2, sheet.max_row +1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * 0.94
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet, min_row=2, max_row=sheet.max_row, min_col=4, max_col=4)
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'b10')
#     wb.save('trash holder.xlsx')
#
class Customer(object):
    all = []

    def __init__(self, name, membership_type='SILVER'):
        self.name = name
        self.membership_type = membership_type
        Customer.all.append(self.name)

    def upgrade_membership(self, new_membership):
        if new_membership.upper() != self.membership_type:
            if self.membership_type != 'Gold':
                self.membership_type = new_membership
                print('Upgrading  to {} ..... \n Successful '.format(self.membership_type))

            else:
                print('Cant upgrade membership as {} is the highest of them all'.format(new_membership))
        else:
            print(' Sorry cant upgrade to {}, because that is your cuurent status. \n  you can either upgrade to '
                  'Gold or downgrade to Bronze'.format(self.membership_type))

    def down_grade_membership(self, new_membership):
        if self.membership_type != 'Silver':
            self.membership_type = new_membership
            print('Downgrading to {} .... \n Successful'.format(self.membership_type))

        else:
            print('Cant Downgrade membership as {} is the lowest of them all'.format(new_membership))

    def membership(self):
        print('this is your current membership satus: {} \n what will you like to do'.format(self.membership_type))
        col = input('Enter Upgrade to Upgrade \n Enter Downgrade to Downgrade\n\t>>')
        if col.upper() == 'UPGRADE':
            status = input('Enter the Status you wish to upgrade to: ')
            self.upgrade_membership(status)
        elif col.upper() == 'DOWNGRADE':
            status = input('Enter the status you wish to downgrade to: ')
            self.down_grade_membership(status)
        else:
            print('Sorry wrong input')

    def __str__(self):
        return 'Congratulations {} Your new membership status is: {}'.format(self.name, self.membership_type)

    @staticmethod
    def print_all_customers(customers):
        return all


c1 = Customer('Bob')
c2 = Customer('Aisha')

c1.membership()
print(c1)
c2.membership()
print(c2)

input("Press enter to quit")





































