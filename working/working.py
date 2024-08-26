import re


def main():
    print(convert(input("Hours: ")))


def format_time(time):
    if ":" in time:
        return time
    else:
        time = time + ":00"
        return time


def convert(time):

    parts = time.split("to ")
    if len(parts) != 2:
        raise ValueError("ValueError")

    a, b = time.split("to ")
    a = a.upper().strip()
    b = b.upper().strip()

    pattern_start = r"^(0?[1-9]|1[0-2])(:[0-5][0-9])?\s*AM$"
    pattern_end = r"^(0?[1-9]|1[0-2])(:[0-5][0-9])?\s*PM$"
    match_a_start = re.search(pattern_start, a)
    match_a_end = re.search(pattern_end, a)
    match_b_start = re.search(pattern_start, b)
    match_b_end = re.search(pattern_end, b)

    if match_a_start:
        time_a, tail_a = a.split(" ")
        hour_a, minute_a = format_time(time_a).split(":")
        if match_b_end:
            time_b, tail_b = b.split(" ")
            hour_b, minute_b = format_time(time_b).split(":")

            if 1 <= int(hour_a) <= 9:
                hour_b = int(hour_b) + 12
                return f"0{hour_a}:{minute_a} to {hour_b}:{minute_b}"
            elif 10 <= int(hour_a) <= 11:
                hour_b = int(hour_b) + 12
                return f"{hour_a}:{minute_a} to {hour_b}:{minute_b}"
            elif int(hour_a) == 12:
                hour_a = int(hour_a) - 12
                hour_b = int(hour_b)
                return f"0{hour_a}:{minute_a} to {hour_b}:{minute_b}"
    elif match_a_end:
        time_a, tail_a = a.split(" ")
        hour_a, minute_a = format_time(time_a).split(":")

        if match_b_start:
            time_b, tail_b = b.split(" ")
            hour_b, minute_b = format_time(time_b).split(":")
            if 1 <= int(hour_b) <= 9:
                hour_a = int(hour_a) + 12
                return f"{hour_a}:{minute_a} to 0{hour_b}:{minute_b}"
            elif 10 <= int(hour_b) <= 11:
                hour_a = int(hour_a) + 12
                return f"{hour_a}:{minute_a} to {hour_b}:{minute_b}"
            elif int(hour_b) == 12:
                hour_a = int(hour_a)
                hour_b = int(hour_b) - 12
                return f"{hour_a}:{minute_a} to 0{hour_b}:{minute_b}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
