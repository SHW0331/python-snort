def add_snort() :
    action = input("Enter action () : ")
    protocol = input("Enter protocol () : ")
    src_ip = input("Enter source ip () : ")
    src_port = input("Enter source port () : ")
    direction = input("Enter direction : ")
    dst_ip = input("Enter destination ip () : ")
    dst_port =input("Enter destination port () : ")
    
    options = []
    while True:
        
        option = input('Enter an option (msg:"option exmaple"; or "done" to finish) : ')

        if option.lower() == 'done':
            break 

        options.append(option)

    option_str = ' '.join(options)
    option = f"({option_str})"

    rule = f"{action} {protocol} {src_ip} {src_port} {direction} {dst_ip} {dst_port} {option}"

    return rule

test = add_snort()
print(test)