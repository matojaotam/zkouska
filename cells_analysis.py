import json

def load_samples(filename):
    samples = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")

            name = parts[0]
            values = []

            for x in parts[1:]:
                values.append(int(x))

            samples[name] = values

    return samples


def calculate_growth_rate(values):
    differences = []

    for i in range(len(values) - 1):
        diff = values[i+1] - values[i]
        differences.append(diff)

    first = differences[0]

    for d in differences:
        if d != first:
            return None

    return first

def create_sample_summary(values, growth_rate):
    summary = {}

    summary["values"] = values
    summary["average"] = sum(values) / len(values)
    summary["min"] = min(values)
    summary["max"] = max(values)
    summary["growth_rate"] = growth_rate

    return summary

def save_results(summary, filename):
    with open(filename, "w") as file:
        json.dump(summary, file, indent=4)


def main():
    data = load_samples("samples.csv")

    summary = {}

    for name in data:
        values = data[name]
        growth = calculate_growth_rate(values)
        sample_summary = create_sample_summary(values, growth)
        summary[name] = sample_summary

    save_results(summary, "results.json")


if __name__ == "__main__":

    main()
    print("Analýza buněk dokončena. Výsledky uloženy do results.json.")

