from monobank import Client


def get_info(token: str):
    full_info = Client(token).get_client_info()
    needed_keys = ('balance', 'type')
    accounts = full_info['accounts']
    info = [{key: account.get(key) for key in needed_keys} for account in accounts]

    message_text = '\n'.join(list(map(lambda account: f'Type - {account["type"]}\nBalance - {account["balance"]}\n' if account["balance"] != 0 else '', info)))
    return message_text
