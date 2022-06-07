from scripts.helpful_scripts import get_account, get_contract
from brownie import Lottery


def deploy_lottery():
    account = get_account(id="vaibhav-brownie")
    lottery = Lottery.deploy(get_contract())
    lottery.wait(1)
    print(lottery)


def main():
    deploy_lottery()
