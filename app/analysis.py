def analyze_waste(fill_level, temperature):

    if temperature > 60:
        condition = "ABNORMAL"
    else:
        condition = "NORMAL"

    if fill_level >= 90:
        priority = "HIGH"
    elif fill_level >= 70:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    return condition, priority