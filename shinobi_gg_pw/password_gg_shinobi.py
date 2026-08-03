def generate_password(
    blue_ninja=False,
    yellow_ninja=False,
    pink_ninja=False,
    green_ninja=False,
    yellow_crystal=False,
    green_crystal=False,
    blue_crystal=False,
    pink_crystal=False,
    health=4
):
    # -------------------------
    # Build ninja bitfield (N)
    # -------------------------
    N = 0

    if blue_ninja:
        N |= 0x1

    if yellow_ninja:
        N |= 0x2

    if pink_ninja:
        N |= 0x4

    if green_ninja:
        N |= 0x8

    # -------------------------
    # Build crystal bitfield (C)
    # -------------------------
    C = 0

    if yellow_crystal:
        C |= 0x1

    if green_crystal:
        C |= 0x2

    if blue_crystal:
        C |= 0x4

    if pink_crystal:
        C |= 0x8

    # -------------------------
    # Convert desired health
    # into health bitfield (H)
    # -------------------------
    health_to_bits = {
        4: 0x0,
        6: 0x1,
        8: 0x3,
        10: 0x7,
        12: 0xF,
    }

    if health not in health_to_bits:
        raise ValueError(
            "Health must be one of: 4, 6, 8, 10, 12"
        )

    H = health_to_bits[health]

    # -------------------------
    # Auto-select key
    # -------------------------
    K = 1

    # -------------------------
    # Encode password
    # -------------------------
    P0 = (N - (2 * K)) & 0xF
    P1 = C
    P2 = (H + K) & 0xF
    P3 = (N + C + H) & 0xF
    P4 = K

    return f"{P0:X}{P1:X}{P2:X}{P3:X}{P4:X}"


# Example:
password = generate_password(
    blue_ninja=True,
    yellow_ninja=True,
    pink_ninja=True,
    green_ninja=True,
    yellow_crystal=True,
    green_crystal=True,
    blue_crystal=True,
    pink_crystal=True,
    health=12
)

print(password)