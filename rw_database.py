# This module must be replaced by database integration
# communication with user database must have very strong security and authentication


from pathlib import Path


def save_sender(sid, name, icons, cell):
    database_path = Path.cwd().joinpath("project_files", "users_database")
    database_append = open(database_path, "a")
    database_append.write(sid + "*%" + name + "*%" + icons + "*%" + cell + "\n")
    database_append.close()

def save_question(qid, num_letters, icons, pos_list):
    database_path = Path.cwd().joinpath("project_files", "question_database")
    database_append = open(database_path, "a")
    list_icons = "%ic_list_".join(icons)
    position_list = "%pos_list_".join(pos_list)
    database_append.write(qid + "*%" + num_letters + "*%" + list_icons + "*%" + position_list + "\n")
    database_append.close()

def save_answer(senderid, answer,questionid):
    database_path = Path.cwd().joinpath("project_files", "answer_database")
    database_append = open(database_path, "a")
    database_append.write(str(senderid) + "*%" + str(answer) + "*%" + str(questionid) + "\n")
    database_append.close()

def string_to_list(string):
    # change string to list
    del_bracket = string.lstrip('[').rstrip(']')
    li = list(del_bracket.split(","))
    return li

def get_sender_info(required_id):
    sender_id = 0
    sender_name = ''
    sender_icons = []
    sender_cell = 0
    user_found = False
    database_path = Path.cwd().joinpath("project_files", "users_database")
    with open(database_path, "rt") as user_info:
        for line in user_info:
            line_split = line.split('*%')
            sender_id = int(line_split[0])
            if sender_id == required_id:
                sender_name = line_split[1]
                sender_icons = [int(i) for i in string_to_list(line_split[2].rstrip('\n'))]
                sender_cell = int(line_split[3])
                user_found = True
                break
        if not user_found:
            print("User not found")
    return sender_id, sender_name, sender_icons, sender_cell
