# Main program used to request the decryption of the answer
# This module must run in a secure environment since it uses private user information

import me_components, me_decoder_client_communicator, me_get_sender_info, me_translator


def main():

    ALPHABET_SIZE = 4
    ALPHABET_FILE = "public_alphabet"

    # Wait for request to decrypt an answer
    communicator_client = me_decoder_client_communicator.ClientCommunicator()
    communicator_client.wait_for_request()

    # Receive the original question, the user id, and the answer to decrypt
    communicator_client.receive_request_info()

    # Get the private user information
    user = me_components.Sender(0, '')
    [user.id, user.name, user.icons, user.cell] = me_get_sender_info.get_sender_info(communicator_client.senderid)

    # Read the public alphabet
    current_translator = me_translator.Translator(ALPHABET_SIZE)
    current_translator.set_alphabet(ALPHABET_FILE)

    # Find the icon used for each letter
    # and the index of the alphabet used for each letter
    icons_used = []
    alph_used = []
    for num_letter in range(communicator_client.question.num_answer_letters):
        icons_used.append(user.find_icon(communicator_client.question.pos_list_set[num_letter].list))
        alph_used.append(communicator_client.question.icons_set[num_letter].find_group(icons_used[num_letter], ALPHABET_SIZE))

    # Decrypt the answer an send the answer decrypted
    plain_answer = current_translator.translate(communicator_client.answer, alph_used)

    # Send answer to client
    communicator_client.send_answer(plain_answer)


if __name__ == "__main__":
    main()
