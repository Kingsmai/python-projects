import math

# 1 Pumpkin Producer = (20 Plate * 9)Stack + 6 Anti + 6 Carved
pumpkin = 1714349
anti = 0
carved = anti
plate = 2
pumpkinProducer = math.floor((pumpkin + anti + carved + (plate * 9)) / 192)
print(f"""
You can craft {pumpkinProducer} pumpkin producers.
You need to craft
    {(pumpkinProducer * 6) - anti} more anti-pumpkin
    {(pumpkinProducer * 6) - carved} more carved-pumpkin
    AND
    {(pumpkinProducer * 20 * 9)} more stacked pumpkin for
    {(pumpkinProducer * 20)} Pumpkin plate.
""")