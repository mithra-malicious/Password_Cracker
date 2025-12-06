import random, string, argparse

Pools =[
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits,
    string.punctuation
]
def generatepassword(length=12):
    password = []
    for pool in Pools:
        password.append(random.choice(pool))

    all_chars = ''.join(Pools)
    while len(password) < length:
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)
parser = argparse.ArgumentParser(description='Generate a random password')
parser.add_argument ('-l', '--length', type=int, default=12, help='Password Length (Deafault=12)')
args = parser.parse_args()
print(generatepassword(args.length))
    
