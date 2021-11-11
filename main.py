import json

def actions_define():
    FILENAME = 'actions.json'
    action_file = open(FILENAME,mode='r')
    data = json.load(action_file)
    action_file.close()
    json_data = data['MainFunctions']
    main_function_keys = json_data.keys()

    for func in main_function_keys:
        func_name = func
        func_data = json_data[func]
        func_type = func_data['Type']
        func_args = func_data['Args']

        print(len(func_args))

        if func_type == 'Function':
            print(func_data['In'] + " = " + func_name)
            condition_value = func_data['Condition']['Value']
            condition_type = func_data['Condition']['Type']
            condition_do = func_data['Condition']['Do']

            if condition_type == 'String':
                condition_value = "\"" + condition_value + "\""

            print("  If " + func_name + "=" + condition_value + " Then")
            print("    " + condition_do)
            print("  End If")

if __name__=='__main__':
    # variable_define()
    actions_define()