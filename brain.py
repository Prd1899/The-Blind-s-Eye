import tell_time, general_conversations, sleep,define_subject
import os
def brain1(speech_text):
    def check_message(check):
        """
        This function checks if the items in the list (specified in argument) are present in the user's input speech.
        """
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False
    if check_message(['who','are', 'you']):
        general_conversations.who_are_you()

    elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
        general_conversations.how_am_i()

    elif check_message(['tell', 'joke']):
        general_conversations.tell_joke()

    elif check_message(['who', 'am', 'i']):
        general_conversations.who_am_i(name)

    elif check_message(['where', 'born']):
        general_conversations.where_born()

    elif check_message(['how', 'are', 'you']):
        general_conversations.how_are_you()

    elif check_message(['time']):
        tell_time.what_is_time()

    elif check_message(['sleep']):
        sleep.go_to_sleep()

    elif check_message(['hello']):
        general_conversations.hello()

    elif check_message(['scan']):
        general_conversations.scan()

    elif check_message(['What','is','weather']):
        general_conversations.what_is_weather()

    elif check_message(['recognise']):
        general_conversations.rec()

    elif check_message(['define']):
        define_subject.define_subject(speech_text)

    else:
        general_conversations.undefined()
