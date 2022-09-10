def print_full_name(first, last):
    # Write your code here
    name=first
    lname=last
    reply="Hello {0}{1}! You just deleved into python"
    print(reply.format(name,lname))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)