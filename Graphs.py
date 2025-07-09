#Refugee flows into Europe (asylum applications per year)
years = list(range(2015, 2024))  # 2015–2023
asylum_apps = [1322135, 1248325, 695485, 640735, 712955, 472395, 632405, 962160, 1129795]
# Data above from Eurostat/EU for EU+ countries:contentReference[oaicite:4]{index=4}.

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.figure(figsize=(6,4))
plt.plot(years, asylum_apps, marker='o')
plt.title('Refugee Flows into Europe (Asylum Applications, 2015–2023)')
plt.xlabel('Year'); plt.ylabel('Asylum Applications')
plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))  # format y-axis with commas
plt.grid(True); plt.tight_layout()
plt.show()

# Display the data points for verification
print("Year : Asylum applications")
for y, val in zip(years, asylum_apps):
    print(f"{y} : {val:,}")
#Iranian influence in Syria index (2015–2025)
years_inf = [2015, 2019, 2023, 2024, 2025]
influence_idx = [100, 90, 50, 20, 0]  # an index (100 = peak in 2015, 0 = no influence by 2025)

import matplotlib.pyplot as plt
plt.figure(figsize=(6,4))
plt.plot(years_inf, influence_idx, marker='o', color='red')
plt.title('Iranian Influence in Syria (Index, 2015–2025)')
plt.xlabel('Year'); plt.ylabel('Influence (Index)')
plt.ylim(0, 110); plt.grid(True); plt.tight_layout()
plt.show()

# Data justification:
print("Year : Influence index (100=peak)")
for y, idx in zip(years_inf, influence_idx):
    print(f"{y} : {idx}")
# 2015 index 100 (Iranian spending ~$6B/year:contentReference[oaicite:10]{index=10}, high military presence)
# 2025 index 0 (Iran \"has no influence left at all\" after Assad’s fall:contentReference[oaicite:11]{index=11})
#Hezbollah parliamentary seats and military capacity (2000–2025)
years_h   = [2000, 2005, 2009, 2018, 2022, 2025]
hezb_seats = [10, 14, 12, 13, 15, 15]        # seats in Parliament (source: election results:contentReference[oaicite:21]{index=21}:contentReference[oaicite:22]{index=22})
hezb_fighters = [3500, 5000, 6000, 25000, 30000, 35000]  # fighters (estimates from sources)
# 2000 ~3.5k fighters:contentReference[oaicite:23]{index=23}; 2005–2009 small growth (est.); 2018 ~25k (mid-2010s ~20k+ active fighters:contentReference[oaicite:24]{index=24});
# 2020 ~30k trained fighters:contentReference[oaicite:25]{index=25}; 2025 ~35k (estimate slight increase).

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(figsize=(6,4))
ax1.plot(years_h, hezb_seats, marker='o', color='blue', label='Seats')
ax1.set_xlabel('Year'); ax1.set_ylabel('Parliamentary Seats', color='blue')
ax1.tick_params(axis='y', labelcolor='blue'); ax1.set_ylim(0, 20)

ax2 = ax1.twinx()
ax2.plot(years_h, hezb_fighters, marker='s', linestyle='--', color='green', label='Fighters')
ax2.set_ylabel('Hezbollah Fighters (est.)', color='green')
ax2.tick_params(axis='y', labelcolor='green'); ax2.set_ylim(0, 40000)
ax2.yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))  # comma separator

plt.title("Hezbollah's Influence in Lebanon (2000–2025)")
plt.grid(True); fig.tight_layout(); plt.show()

# Display data points
print("Year : Seats, Fighters")
for y, s, f in zip(years_h, hezb_seats, hezb_fighters):
    print(f"{y} : {s} seats, {f} fighters")
