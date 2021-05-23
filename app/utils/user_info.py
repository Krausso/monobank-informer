from monobank import Client


def get_info(token: str):
    full_info = Client(token).get_client_info()
    needed_keys = ('balance', 'type')
    accounts = full_info['accounts']
    info = [
        {key: account.get(key) for key in needed_keys}
        for account in accounts
    ]

    message_text = ''
    for account in info:
        account_type, account_balance = account["type"], account["balance"]

        if account_balance != 0:
            message_text += f'\nType - {account_type}.\nBalance: {str(account_balance)[:-2]}\n'

    return message_text
