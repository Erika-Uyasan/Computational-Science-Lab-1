from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN

# 1. SETUP: High-precision environment
getcontext().prec = 150  

# Pi to 100 decimals
PI_100 = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

def get_volume_multiplier(radius):
    return (Decimal(4) / 3) * (Decimal(radius) ** 3)

# 2. LAB PARAMETERS
intervals = [20, 40, 60, 80, 100]
radius = 5
multiplier = get_volume_multiplier(radius)

# Using 100-decimal Pi as our "True" value
v_true = multiplier * PI_100

print(f"{'PRECISION':<12} | {'TRUNCATED VOLUME':<45} | {'ERROR VS TRUE'}")
print("-" * 85)

history = []

# 3. EXECUTION LOOP
for d in intervals:
    shift = Decimal(10)**-d
    pi_trunc = PI_100.quantize(shift, rounding=ROUND_DOWN)
    pi_round = PI_100.quantize(shift, rounding=ROUND_HALF_UP)
    
    v_trunc = multiplier * pi_trunc
    v_round = multiplier * pi_round
    
    # How much of the "true" volume are we missing?
    rel_error = (v_true - v_trunc) / v_true
    
    print(f"{d:<3} decimals | {str(v_trunc)[:43]:<45} | {rel_error:.2e}")
    
    history.append({'d': d, 'v_t': v_trunc, 'v_r': v_round})

# 4. PROPAGATION ANALYSIS
print("\n" + "="*85)
print(f"{'STAGE GAP':<25} | {'TRUNCATION CHANGE':<25} | {'ROUNDING CHANGE'}")
print("="*85)

for i in range(1, len(history)):
    prev, curr = history[i-1], history[i]
    
    # Calculating the physical change between stages
    change_t = curr['v_t'] - prev['v_t']
    change_r = curr['v_r'] - prev['v_r']
    
    label = f"{prev['d']} -> {curr['d']} digits"
    # Format with '+' to show direction of change clearly
    print(f"{label:<25} | {change_t:+.2e} {'':<16} | {change_r:+.2e}")