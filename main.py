import argparse
import socket
import sys
import subprocess
import requests
import json
import time
import os
import random


verbose = False
os.system("clear")
logo = """

                        88
                        88
                        88
 ,adPPYba,   ,adPPYba,  88,dPPYba,    ,adPPYba,
a8P_____88  a8"     ""  88P'    "8a  a8"     "8a
8PPEECHO""  8b          88       88  8b       d8
"8b,   ,aa  "8a,   ,aa  88       88  "8a,   ,a8"
 `"Ybbd8"'   `"Ybbd8"'  88       88   `"YbbdP"'
                                             by Astra
─────────────────────────────────────────────────────
𝙴𝚌𝚑𝚘 — 𝚢𝚘𝚞𝚛 𝚙𝚎𝚛𝚜𝚘𝚗𝚊𝚕 𝙾𝚂𝙸𝙽𝚃 𝚝𝚘𝚘𝚕
─────────────────────────────────────────────────────
                                                     """
logo2 ="""
⠀⠀⠀⠀⠀⠀⠀⠠⡧⠀⠀⠀⠄⠀⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡄⠀⠀⠀⢺⠂⠀⠀⠀⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣧
⠀⠐⠗⠀⠀⠀⠀⠁⠀⠀⠀⣼⣿⡏⣿⣷⡀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠐⠺⠂⠀⠀⠀⠀⠀⠀⠄
⠤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⠇⠀⢿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒
⠀⠀⠘⢿⣿⣿⣟⠛⠛⠛⠛⠀⠀⠀⠛⠛⠛⠛⠋⠉⠉⠉
⠀⠀⠁⠀⠈⠛⣿⣿⣦
⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿      01100101 01100011 01101000 01101111
⠀⠀⠀⠠⡧⠀⠀⣾⣿⠁⢀⣤⣾⣦⡀
⠀⠠⠀⠀⠀⠀⣸⣿⢇⣶⣿⠟⠙⠻⣿⣄
⠀⠀⠀⠀⠀⢠⣿⣿⠿⠋⠁⠀⠀⠀⠀⠉⠳⡄
⠀⠀⠀⠀⠀⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
─────────────────────────────────────────────────────
𝙴𝚌𝚑𝚘 — 𝚢𝚘𝚞𝚛 𝚙𝚎𝚛𝚜𝚘𝚗𝚊𝚕 𝙾𝚂𝙸𝙽𝚃 𝚝𝚘𝚘𝚕
─────────────────────────────────────────────────────
"""

num = random.randint(0,1)
if num == 1:
    logos = logo2
else:
    logos = logo

for line in logos.splitlines():
    print(line)
    time.sleep(0.2)

parser = argparse.ArgumentParser(description="scry")
parser.add_argument("-n", "--name", help="Full name of a subject", default="-")
parser.add_argument("-u", "--username", help="Username of Subject", default="-")
parser.add_argument("-p", "--phone", help="Subject's phonenumber", default="-")
parser.add_argument("-w", "--website", help="Subject's website", default="-")
parser.add_argument("-i", "--ip", help="Subject's IP address", default="-")
parser.add_argument("-P", "--password", help="Subject's IP address", default="-")
parser.add_argument("-e", "--email", help="Email address", default="-")
args = parser.parse_args()

data = [args.name , args.username, args.phone, args.website, args.ip, args.password]
fields = ["uuid","password","discordid","steamid","domain","phone","email","ip","name","username"]
all_results = []
dataz = [
    (args.name, "name"),
    (args.username, "username"),
    (args.phone, "phone"),
    (args.email, "email"),
    (args.website, "website"),
    (args.ip, "ip"),
    (args.password, "password"),
]

fields = []

for value, field in dataz:
    if value != "-":
        fields.append(field)

lines = [
    f"Full Name: {args.name}",
    f"Username: {args.username}",
    f"Email: {args.email}",
    f"Phone Number: {args.phone}",
    f"Website: {args.website}",
    f"IP Address: {args.ip}",
    f"Password : {args.password}"
]

max_length = max(len(line) for line in lines)
box_width = max_length + 2  # padding 1 space on each side

top_left = "┌"
top_right = "┐"
bottom_left = "└"
bottom_right = "┘"
horizontal = "─"
vertical = "│"

print(f"{top_left}{horizontal * box_width}{top_right}")

for line in lines:
    print(f"{vertical} {line.ljust(max_length)} {vertical}")

print(f"{bottom_left}{horizontal * box_width}{bottom_right}")

print("\n[?] Is this information correct? 𝖸/𝖭")
validate = input(">>:")

if validate.lower() == "n":
    print("Please re-run the program")
    exit()

os.system("clear")

num = random.randint(0,1)
if num == 1:
    logos = logo2
else:
    logos = logo

for line in logos.splitlines():
    print(line)
    time.sleep(0.2)

max_length = max(len(line) for line in lines)
box_width = max_length + 2  # padding 1 space on each side

top_left = "┌"
top_right = "┐"
bottom_left = "└"
bottom_right = "┘"
horizontal = "─"
vertical = "│"

print(f"{top_left}{horizontal * box_width}{top_right}")

for line in lines:
    print(f"{vertical} {line.ljust(max_length)} {vertical}")

print(f"{bottom_left}{horizontal * box_width}{bottom_right}")


print("[i] Variables set!")
print("[i] Forming Payload . . .")
time.sleep(1)
import requests

json_whole_dump = []  # this will hold ALL responses

for term, field in dataz:
    # skip invalid terms
    if term == "-" or not term:
        continue

    payload = {
        "term": getattr(args, field, None),  # dynamically get args.field
        "fields": [field],                   # search ONE field at a time
        "categories": [],
        "wildcard": True,
        "case_sensitive": False
    }

    # skip empty values like "-"
    if not payload["term"] or payload["term"] == "-":
        continue
    print("[i] Sending Request to api-1")
    response = requests.post(
        "https://breach.vip/api/search",
        headers={"Content-Type": "application/json"},
        json=payload
    )

    if response.status_code == 200:
        data = response.json()
        print(f"[i] Received Response for field {field}")

        # store with field name so you know what came from where
        json_whole_dump.append({
            "field": field,
            "term": payload["term"],
            "result": data
        })
        results = data.get("results", [])
        all_results.extend(results)
    else:
        print(f"[!] Error for field '{field}': {response.status_code}")

def first(item, keys):
    for k in keys:
        if k in item and item[k]:
            return item[k]
    return None

results = all_results






merged = []
index = {}  # value -> entry

def normalize_value(val):
    """Convert lists to tuples so they can be added to sets."""
    if isinstance(val, list):
        return tuple(val)
    return val

def get_or_create_entry(values):
    for v in values:
        v = normalize_value(v)
        if v and v in index:
            return index[v]

    entry = {
        "names": set(),
        "usernames": set(),
        "emails": set(),
        "phones": set(),
        "ips": set(),
        "passwords": set(),
        "sources": set(),
    }
    merged.append(entry)
    return entry


for item in results:
    email = item.get("email")
    password = first(item, ["password", "hashedpassword", "hash"])
    username = first(item, ["username", "﻿username", "discord_tag"])
    name = first(item, ["name", "FullNameOrUserName", "firstname", "fname"])
    phone = item.get("phone")
    ip = first(item, ["ip", "join_time"])
    website = item.get("source")

    # skip empty rows
    if not any([email, password, username, name, phone, ip]):
        continue

    values = [email, password, username, name, phone, ip]
    values = [normalize_value(v) for v in values]
    entry = get_or_create_entry(values)

    # merge values
    if name:
        entry["names"].add(normalize_value(name))
        index[normalize_value(name)] = entry

    if username:
        entry["usernames"].add(normalize_value(username))
        index[normalize_value(username)] = entry

    if email:
        entry["emails"].add(normalize_value(email))
        index[normalize_value(email)] = entry

    if phone:
        entry["phones"].add(normalize_value(phone))
        index[normalize_value(phone)] = entry

    if ip:
        entry["ips"].add(normalize_value(ip))
        index[normalize_value(ip)] = entry

    if password:
        entry["passwords"].add(normalize_value(password))
        index[normalize_value(password)] = entry

    if website:
        entry["sources"].add(normalize_value(website))







#
def flatten_value(v):
    """Convert anything (list, tuple, number) to string for printing."""
    if isinstance(v, (list, tuple, set)):
        return ", ".join(str(x) for x in v)
    return str(v)

top_left = "┌"
top_right = "┐"
bottom_left = "└"
bottom_right = "┘"
horizontal = "─"
vertical = "│"

print("""
─────────────────────────────────────────────────────
𝚁𝚎𝚜𝚞𝚕𝚝 :
─────────────────────────────────────────────────────
""")
for i, entry in enumerate(merged, 1):
    lines = []

    def format_lines(label, values):
        # Ensure values is a list of full strings
        # If flatten_value returns a string, wrap it in a list
        if isinstance(values, str):
            values = [values]
        return [f"{label} : {v}" for v in values]

    if entry["names"]:
        lines.extend(format_lines("names     ", entry["names"]))
    if entry["usernames"]:
        lines.extend(format_lines("usernames ", entry["usernames"]))
    if entry["emails"]:
        lines.extend(format_lines("emails    ", entry["emails"]))
    if entry["phones"]:
        lines.extend(format_lines("phones    ", entry["phones"]))
    if entry["ips"]:
        lines.extend(format_lines("ips       ", entry["ips"]))
    if entry["passwords"]:
        lines.extend(format_lines("passwords ", entry["passwords"]))
    if entry["sources"]:
        lines.extend(format_lines("sources   ", entry["sources"]))

    if not lines:
        continue

    max_length = max(len(line) for line in lines)
    box_width = max_length + 2
    num = random.random()
    time.sleep(num)
    # Print top border
    print(f"{top_left}{horizontal * box_width}{top_right}")

    # Print content lines
    for line in lines:
        print(f"{vertical} {line.ljust(max_length)} {vertical}")

    # Print bottom border
    print(f"{bottom_left}{horizontal * box_width}{bottom_right}")



# ===== VERBOSE DUMP =====
print("\n" + "="*80)
print("VERBOSE SUMMARY OF VARIABLES AND DATA STRUCTURES")
print("="*80)

def dump_var(name, var):
    try:
        # try pretty-print JSON-style
        print(f"\n{name} = {json.dumps(var, indent=2, default=str)}")
    except Exception:
        # fallback
        print(f"\n{name} = {repr(var)}")

if verbose:
    dump_var("args", vars(args))
    dump_var("dataz", dataz)
    dump_var("fields", fields)
    dump_var("lines", lines)
    dump_var("json_whole_dump", json_whole_dump)
    dump_var("results", results)
    dump_var("all_results", all_results)
    dump_var("merged", merged)
    dump_var("index", {k: str(v) for k, v in index.items()})  # convert sets to string for readability


#dump_var("args", vars(args))
#dump_var("dataz", dataz)
#dump_var("fields", fields)
#dump_var("lines", lines)
#d#ump_var("json_whole_dump", json_whole_dump)
#d#ump_var("results", results)
#d#ump_var("all_results", all_results)
#dump_var("merged", merged)
#dump_var("index", {k:str(v) for k,v in index.items()})  # convert sets to string for readability

print("\n" + "="*80)
print("END OF VERBOSE DUMP")
print("="*80)
