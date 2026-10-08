# The while loop keeps happening until the condition is False
def annoying_roomate():
    can_i_borrow = input("Can I borrow your sweater? ")
    while can_i_borrow != "yes":
        can_i_borrow = input("Can I borrow your sweater? ")

#Make the condition always True and use the Break keybord
def annoying_roomate_2():
    while True:
        can_i_borrow = input("Can I borrow your sweater? ")
        if can_i_borrow == "Yes":
            break

def bad_dont_do_this():
    while True:
        print("I love you")
        print("FOREVER")

def main():
    # annoying_roomate()
    # annoying_roomate_2()
    bad_dont_do_this()
main()
