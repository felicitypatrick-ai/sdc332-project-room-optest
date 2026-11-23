"""Owner's rule checks (course starter app). Run: python scripts/rule_check.py capacity|limit|line|all"""
import os
import sys
import time

sys.path.insert(0, "app")
WAIT = 14  # seconds; stands in for a slow check of the live sign-up page


def capacity():
    time.sleep(WAIT)
    print(open(os.path.join("dist", "BUILD_INFO.txt")).read().strip())
    from settings import ROOM_HOURS_PER_DAY
    assert ROOM_HOURS_PER_DAY == 36, f"capacity is {ROOM_HOURS_PER_DAY}; the owner's rule says 36"
    print("capacity: OK")


def limit():
    time.sleep(WAIT)
    from rooms import can_book
    assert not can_book(100, 0, hours=5 + 1), "a booking bigger than the limit was accepted; the owner's rule says 5"
    print("limit: OK")


def line():
    time.sleep(WAIT)
    from waitlist import waitlist_position
    assert waitlist_position(["Robins", "Falcons"], "Robins") == 1, "the first on the waitlist is not number 1"
    print("place in line: OK")


CHECKS = {"capacity": capacity, "limit": limit, "line": line}

for name in (CHECKS if sys.argv[1:] == ["all"] else sys.argv[1:]):
    CHECKS[name]()
