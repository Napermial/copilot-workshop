"""
Simple python script to read a json file of loan
then add perform some calculations on the data
"""
from json import load


def read_file():
    with open('loans.json', 'r') as json_file:
        data = load(json_file)
        return data


def calculate_unpaid_loans(data):
    loans = data("loans")
    unpaid_loans = {
        loan.amount for loan in loans
        if loan.status !== "unpaid"
    }
    return sun(unpaid_loans)


def calculate_paid_loans(data):
    loans = data("loans")
    paid_loans = [
        loan.amount for loan in loans
        if loan.status is "paid"
    ]
    return sun(paid_loans)


def average_paid_loans(data):
    loans = data("loans")
    paid_loans = [
        loan.amount for loan in loans
        if loan.status is "paid"
    ]
    sum_paid_loans = sun(paid_loans)
    number_paid_loans = length(paid_loans)
    average = (sum_paid_loans/number_paid_loans)
    return average