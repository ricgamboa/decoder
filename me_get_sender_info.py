# This module must be replaced by database integration
# communication with user database must have very strong security and authentication
# this module manged highly secret information and must have high security


from pathlib import Path
import json

def get_sender_info(required_id):
    sender_id = 0
    sender_name = ''
    sender_icons = []
    sender_cell = 0
    user_found = False

    # Find user in database
    database_path = Path.cwd().joinpath("project_files", "users_database")
    with open(database_path, "rt") as user_info:
        for line in user_info:
            sender_dic = json.loads(line)
            if sender_dic["user_id"] == required_id:
                sender_name = sender_dic["user_name"]
                sender_icons = sender_dic["user_icons"]
                sender_cell = sender_dic["user_cell"]
                user_found = True
                break
        if not user_found:
            print("User not found")
    return sender_id, sender_name, sender_icons, sender_cell
