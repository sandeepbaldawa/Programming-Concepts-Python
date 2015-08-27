def get_look_and_say_helper(input_string="1"):
    prev = -1
    count = 0
    out = ""
    for each_char in input_string:
        if int(each_char) != prev:
            if prev != -1:
                out += str(count) + str(prev)
            count = 0       
            prev = int(each_char)
        count+=1
    out += str(count) + str(prev)
    return out

def get_look_and_say(N):
    ret = "1"
    for _ in xrange(N):
        print ret
        ret = get_look_and_say_helper(ret)

if __name__ == "__main__":
    get_look_and_say(10)
