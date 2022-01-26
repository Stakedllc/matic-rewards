import json
from web3 import Web3

NODE_ENDPOINT = ""
DELEGATED_ADDRESS = ""
VALIDATOR_SHARE_PROXY_ADDRESS = "0x41472fDdbAEc17E2a98F125Cacf8f76F919EA095"

w3 = Web3(Web3.HTTPProvider(NODE_ENDPOINT))

validator_share_abi_file = open('./ValidatorShare.json')
validator_share_abi = json.load(validator_share_abi_file)
contract = w3.eth.contract(address=VALIDATOR_SHARE_PROXY_ADDRESS, abi=validator_share_abi)

validator_id = contract.functions.validatorId().call()
print("Validator ID", validator_id)

delegated_amount = contract.functions.getTotalStake(DELEGATED_ADDRESS).call()
print("Delegated Amount", delegated_amount)

liquid_rewards = contract.functions.getLiquidRewards(DELEGATED_ADDRESS).call()
print("Liquid Rewards", liquid_rewards)