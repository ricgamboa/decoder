# This module must be replaced with communication between the local system and the client,
# the client is the system that only knows the original question, the id of the user, and the encrypted answer, and
# request the decryption of the answer

from pathlib import Path
import def_classes

class ClientCommunicator():

    def __init__(self):
        self.question = def_classes.Question(0, 0)
        self.answer = []
        self.senderid = 0

    def wait_for_request(self):
        input("Press enter to send the request...")

    def string_to_list(self, string):
        # change string to list
        del_bracket = string.lstrip('[').rstrip(']')
        temp_li = list(del_bracket.split(","))
        li = []
        for item in temp_li:
            item = item.strip('\n')
            item = item.strip(']')
            item = item.strip('[')
            li.append(item)
        return li


    def receive_request_info(self):
        # This method must be replaced to receive information
        # from the client
        test_client_info_path = Path.cwd().joinpath("project_files", "test_client_info")
        with open(test_client_info_path, "rt") as client_info:
            line = client_info.readline()
        info_split = line.split('*%')
        self.question.id = int(info_split[0])
        self.question.num_answer_letters = int(info_split[1])
        # save the set of icons in the question
        str_icons = info_split[2].split('%ic_list_')
        for ic_li in range(len(str_icons)):
            temp_icons = self.string_to_list(str_icons[ic_li])
            icons_list = [int(i) for i in temp_icons]
            self.question.append_icon_set(icons_list)
        # save the position list
        str_position = info_split[3].split('%pos_list_')
        for pos_li in range(len(str_position)):
            temp_position = self.string_to_list(str_position[pos_li])
            pos_list = [int(i) for i in temp_position]
            self.question.append_position_list(pos_list)
        # save the user id
        self.senderid = int(info_split[4])
        # save the encrypted answer
        answer_string = self.string_to_list(info_split[5])
        count = 0
        for item in answer_string:
            self.answer.append(item.strip())
            count += 1

    def send_answer(self, answer):
        # This method must be replaced to send answer to the client
        letters = ["a", "b", "c", "d"]
        print("Answer decrypted is:")
        for answer_letter in answer:
            int(answer_letter)
            print(" {} ".format(letters[answer_letter]), end='')
