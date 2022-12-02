def enterPIN(cardNum: str, pin: str) -> bool:
    if pin.isdigit() and len(pin) == 4:
        return True
    else:
        return False
