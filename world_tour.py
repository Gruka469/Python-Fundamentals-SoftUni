def add_stop(stops, index, stop):
    if 0 <= index < len(stops):
        stops = stops[:index] + stop + stops[index:]
    return stops

def remove_stop(stops, start_index, end_index):
    if 0 <= start_index <= end_index < len(stops):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops

def switch_string(stops, old_string, new_string):
    stops = stops.replace(old_string, new_string)
    return stops

stops = input()
command = input()

while command != "Travel":
    command_parts = command.split(":")
    action = command_parts[0]

    if action == "Add Stop":
        index = int(command_parts[1])
        stop = command_parts[2]
        stops = add_stop(stops, index, stop)

    elif action == "Remove Stop":
        start_index = int(command_parts[1])
        end_index = int(command_parts[2])
        stops = remove_stop(stops, start_index, end_index)

    elif action == "Switch":
        old_string = command_parts[1]
        new_string = command_parts[2]
        stops = switch_string(stops, old_string, new_string)

    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
