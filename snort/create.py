def create_snort(path) :

    while True:
        try:
            action = input("Enter action: ")
            if not action:
                raise ValueError("Action is required.")
            
            protocol = input("Enter protocol: ")
            if not protocol:
                raise ValueError("Protocol is required.")
            
            src_ip = input("Enter source IP: ")
            if not src_ip:
                raise ValueError("Source IP is required.")
            
            src_port = input("Enter source port: ")
            if not src_port:
                raise ValueError("Source port is required.")
            
            direction = input("Enter direction: ")
            if not direction:
                raise ValueError("Direction is required.")
            
            dst_ip = input("Enter destination IP: ")
            if not dst_ip:
                raise ValueError("Destination IP is required.")
            
            dst_port = input("Enter destination port: ")
            if not dst_port:
                raise ValueError("Destination port is required.")

            break
        
        except ValueError as e:
            print(f"Error: {e}. Please provide a valid input.")

    options = []
    while True:
        try:
            option = input('Enter an option (e.g., "option example"; or "done" to finish) : ')
            if option.lower() == 'done':
                break

            if not option.endswith(';'):
                raise ValueError("Option should end with a semicolon (;).")

            options.append(option)
        
        except ValueError as e:
            print(f"Error: {e}. Please provide a valid input.")

    option_str = ' '.join(options)
    option = f"({option_str})"

    rule = f"\n{action} {protocol} {src_ip} {src_port} {direction} {dst_ip} {dst_port} {option}\n"

    with open(path, "a") as file:
        file.write(rule)
    print(f'added : {path}')    