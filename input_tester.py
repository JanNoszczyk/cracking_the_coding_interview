from URLify import URLify

def main():
    input_string = str(input('Enter your string:'))
    true_length = int(input('Enter your string length:'))
    # true_length = len(input_string)
    print(URLify(input_string, true_length))

if __name__ == "__main__":
    main()