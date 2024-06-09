import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_card(card_number: str) -> str:
    """Функция возвращает замаскированный номер карты"""
    logger.info(f'Возвращаем замаскированный номер карты')
    mask_number = ""
    if card_number.isdigit() and len(card_number) == 16:
        mask_number = f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    return mask_number


def mask_account(acc_number: str) -> str:
    """Функция возвращает замаскированный номер счёта"""
    logger.info(f'Маскируем номер карты')
    mask_bank_account = ""
    if acc_number.isdigit() and len(acc_number) == 20:
        mask_bank_account = f"{'*' * 2}{acc_number[-4:]}"
    return mask_bank_account
