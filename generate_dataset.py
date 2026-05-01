import numpy as np
import pandas as pd


def generate_house_dataset(n=500, seed=42, output_csv="house_data_ph.csv"):
    rng = np.random.default_rng(seed)

    sizes = rng.integers(40, 250, size=n)
    bedrooms = rng.integers(1, 6, size=n)
    location_scores = rng.integers(1, 11, size=n)

    finish_levels = rng.choice(
        ["basic", "standard", "high_end"],
        size=n,
        p=[0.3, 0.55, 0.15]
    )

    cost_per_sqm = np.array([
        rng.integers(15000, 20001) if finish == "basic"
        else rng.integers(25000, 40001) if finish == "standard"
        else rng.integers(45000, 65001)
        for finish in finish_levels
    ])

    location_multiplier = 1 + (location_scores - 5) * 0.04
    bedroom_extra_cost = bedrooms * rng.integers(30000, 70000, size=n)

    base_construction_cost = sizes * cost_per_sqm
    price = base_construction_cost * location_multiplier + bedroom_extra_cost
    price += rng.normal(0, 80000, size=n)

    df = pd.DataFrame({
        "size_sqm": sizes,
        "bedrooms": bedrooms,
        "location_score": location_scores,
        "finish_level": finish_levels,
        "cost_per_sqm": cost_per_sqm,
        "estimated_price": price.astype(int)
    })

    df.to_csv(output_csv, index=False)
    return df


if __name__ == "__main__":
    df = generate_house_dataset()
    print("Philippines house construction dataset generated!")
    print(df.head())
