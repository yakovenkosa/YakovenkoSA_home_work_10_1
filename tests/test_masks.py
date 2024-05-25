import pytest

from src.masks import mask_card, mask_account


@pytest.mark.parametrize(
    "card_number, mask_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_mask_card(card_number, mask_number):
    assert mask_card(card_number) == mask_number


@pytest.mark.parametrize(
    "acc_number, mask_bank_account",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_mask_account(acc_number, mask_bank_account):
    assert mask_account(acc_number) == mask_bank_account