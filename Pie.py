from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP

# Set work precision slightly higher than baseline to prevent calculation rounding
getcontext().prec = 120 

# Baseline: Pi to 100 decimals as specified in your notes
PI_100 = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

def run_arranged_lab(radius_val):
    r = Decimal(str(radius_val))
    # Formula multiplier: 4/3 * r^3
    multiplier = (Decimal(4) / 3) * (r**3)
    
    # Specific intervals from your handwritten notes
    intervals = [20, 40, 60, 80, 100]
    
    prev_v_trunc = None
    prev_v_round = None

    print(f"\n{'='*75}")
    print(f"{'NUMERICAL PRECISION & ERROR PROPAGATION LAB':^75}")
    print(f"{'Formula: V = (4/3) * pi * r^3 | Radius: ' + str(radius_val):^75}")
    print(f"{'='*75}\n")
    
    print(f"{'DECIMALS':<10} | {'TRUNCATION GAP (ERR)':<30} | {'ROUNDING GAP (ERR)':<30}")
    print(f"{'-'*10} | {'-'*30} | {'-'*30}")

    for p in intervals:
        # Define precision level
        places = Decimal(1).scaleb(-p)
        
        # Method 1: Truncation (Chopping off digits)
        pi_t = PI_100.quantize(places, rounding=ROUND_DOWN)
        
        # Method 2: Rounding (Adjusting the last digit)
        pi_r = PI_100.quantize(places, rounding=ROUND_HALF_UP)
        
        # Calculate Volumes
        v_t = multiplier * pi_t
        v_r = multiplier * pi_r
        
        # Calculate the GAP: Difference from the previous precision stage
        if prev_v_trunc is None:
            gap_t_str = "Baseline (Start)"
            gap_r_str = "Baseline (Start)"
        else:
            gap_t = v_t - prev_v_trunc
            gap_r = v_r - prev_v_round
            # Labels showing the movement in scientific notation
            gap_t_str = f"{gap_t:+.2e} (Gain)"
            gap_r_str = f"{gap_r:+.2e} (Adj)"

        print(f"{p:<10} | {gap_t_str:<30} | {gap_r_str:<30}")

        prev_v_trunc = v_t
        prev_v_round = v_r

    print(f"\n{'='*75}")
    print("ANALYSIS SUMMARY:")
    print("- TRUNCATION GAP: Shows the volume added as chopped digits are restored.")
    print("- ROUNDING GAP: Shows the tiny correction needed at higher precision.")
    print("- SCIENTIFIC NOTATION (e.g., e-41): Indicates values extremely close to zero.")

run_arranged_lab(5)
