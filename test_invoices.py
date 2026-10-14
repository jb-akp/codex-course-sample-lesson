from decimal import Decimal

import pytest

from invoices import total_due


def test_amounts_with_cents():
    total = total_due([
        {"amount": "0.10", "status": "unpaid"},
        {"amount": "0.20", "status": "unpaid"},
    ])
    assert isinstance(total, Decimal)
    assert total == Decimal("0.30")


@pytest.mark.parametrize("status", ["unpaid", "UNPAID", "UnPaId"])
def test_case_insensitive_status(status):
    assert total_due([
        {"amount": "450.25", "status": status},
        {"amount": "300", "status": "PAID"},
    ]) == Decimal("450.25")


@pytest.mark.parametrize("amount", ["", "   "])
def test_blank_amount_skipped_with_warning(amount):
    with pytest.warns(UserWarning, match="Skipping row with blank amount"):
        total = total_due([
            {"amount": amount, "status": "unpaid"},
            {"amount": "1200.50", "status": "unpaid"},
        ])
    assert total == Decimal("1200.50")
