def mask_card(card_number: str) -> str:
    """Функция возвращает замаскированный номер карты"""
    mask_number = ""
    if card_number.isdigit() and len(card_number) == 16:
        mask_number = f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    return mask_number


def mask_account(acc_number: str) -> str:
    """Функция возвращает замаскированный номер счёта"""
    mask_bank_account = ""
    if acc_number.isdigit() and len(acc_number) == 20:
        mask_bank_account = f"{'*' * 2}{acc_number[-4:]}"
    return mask_bank_account
