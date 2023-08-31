def get_file_data(file_name):
    file = open(file_name)
    file_data = file.readlines()
    file.close()    
    return file_data

def extract_functions(file_data):
    fun = []
    i=0
    file_len = len(file_data)
    while i<file_len and " def " not in file_data[i]:
        i+=1
    print(file_data[i])
    one_fun= file_data[i]
    i+=1
    while i<file_len:
        if " def " in file_data[i]:
            fun.append(one_fun)
            one_fun = file_data[i]
        else:
            if "@" not in file_data[i]:
                one_fun+=file_data[i]
        i+=1
    fun.append(one_fun.split("if __name__")[0])

    return fun
# fun = []

def get_functions_from_file(file_names: list):
    funs=[]
    for file_name in file_names:
        # file = open(file_name)
        # file_data = file.readlines()
        # file.close()

        file_data = get_file_data(file_name)

        funs=extract_functions(file_data)
    
    return funs