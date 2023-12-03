import boto3
from botocore.exceptions import ClientError
import logging
import constants
import utils


def get_transactions_by_date():
    '''
    Returns json of transactions from supplied date till current.
    If date is further back than last transaction, returns all transactions
    '''

def get_transactions_by_pfc():
    '''
    Returns json of all transactions that match the personal finance category
    provided.
    '''

def update_transactions():
    '''
    Updates transaction in database for any transactions that have been modified.
    Pass in list of modified transactions, returns success or failure.
    '''

def add_transactions():
    '''
    Adds new transactions to the database. Pass in a list of transactions,
    returns success or failure.
    '''

def remove_transactions():
    '''
    Remove transactions from the database. Pass in list of transaction ids,
    returns success or failure.
    '''

def update_database():
    '''
    Automated job called nightly to retrieve recent transactions from bank, and
    update the datebase with the changes [added, modified, removed].
    '''