import os
import subprocess
from random import random, choice

"""
Generates training and test data files for natural language grounding
"""

# Define synthetic data
# Types of actions
action_synonyms = {"go":    ["go","move","drive","proceed","head"],
                   "find":  ["find","find me","look for","search for","locate","identify"], 
                   "get":   ["get","get me","bring","bring me","fetch","fetch me",
                             "grab","grab me","pick up","retrieve"],
                   "store": ["store","place","put away","put back","clean","clean up","tidy","tidy up",
                             "clear","clear away","throw out","throw away","take"]}
actions = list(action_synonyms.keys())

post_action_modifiers = {"go":    ["to the","by the","toward the","towards the","near the",
                                  "over to the","over by the"],
                         "find":  ["the","a","some"],
                         "get":   ["the","a","some"],
                         "store": ["the","a"]}

obj_location_modifiers = ["in the", "inside the", "by the", "near the", 
                          "from the", "around the", "close to the"]

object_synonyms = {"fruit":     ["apple", "banana", "orange"], 
                   "drink":     ["water", "beverage", "soda"],
                   "snack":     ["chips", "cookies", "crackers"],
                   "unknown":   ["object", "thing", "item"]}
objects = list(object_synonyms.keys())

room_synonyms = {"kitchen":     ["kitchen", "pantry", "canteen"],
                 "living room": ["living room", "parlor", "sitting room"],
                 "bedroom":     ["bedroom", "my room"]}
rooms = list(room_synonyms.keys())

# Other useful data to have for checking and parsing
vowels = ["a", "e", "i", "o", "u"]


def generate_data(out_file, num_samples, do_print=False):
    """
    Generates synthetic data
    """
    f = open(out_file,"w+")
    f.write("Sentence,Action,Room,Object\n")

    # Get the probability of sampling an unknown location
    unknown_loc_prob = 1.0/(len(rooms) + 1)

    num_generated = 0
    generated_sentences = []
    while num_generated < num_samples:

        # Sample groundings
        act = choice(actions)
        act_token = choice(action_synonyms[act])
        obj = choice(objects)
        obj_token = choice(object_synonyms[obj])   
        if random() < unknown_loc_prob:
            loc = "unknown"
        else:
            loc = choice(rooms)
            loc_token = choice(room_synonyms[loc])   

        post_act_mod = choice(post_action_modifiers[act])

        # Special rules... because English
        # If the modifier ends with "a" and the object starts with a vowel, it must be "an"
        if post_act_mod == "a" and obj_token[0] in vowels:
            post_act_mod = "an"

        sent = None

        # Location is unknown
        if loc == "unknown":
            # Object is unknown
            if obj == "unknown":
                pass
            # Object is known
            else:
                # Sentence example: "Bring me some water"
                sent = (act_token + " " + post_act_mod + " " + obj_token)

        # Location is known     
        else:
            # Need another chain of logic since unknown objects mean something different for "Go"
            # Sentence example: "Go to the kitchen"
            if act == "go" and obj == "unknown":
                sent = (act_token + " " + post_act_mod + " " + loc_token)
            # Sentence type: "Find the object near the kitchen"
            else:
                obj_loc_mod = choice(obj_location_modifiers)
                sent = (act_token + " " + post_act_mod + " " + 
                        obj_token + " " + obj_loc_mod + " " + loc_token)

        # Accept the sentence if valid
        # Accepting means writing to file and adding to the list of generated sentences
        if sent is not None and not sent in generated_sentences:
            num_generated += 1
            grounding_line = sent + "," + act + "," + loc + "," + obj + "\n"
            f.write(grounding_line)
            generated_sentences.append(grounding_line)
            if do_print:
                print(str(num_generated) + ": " + grounding_line)

    # Close the file
    f.close()

# Main function
if __name__=="__main__":

    # Get folder information
    cur_dir = os.path.dirname(os.path.abspath(__file__))

    # Set output parameters
    training_file_name = "rnn_training_data.txt"
    num_training_samples = 1000
    test_file_name = "rnn_test_data.txt"
    num_test_samples = 500

    # Generate data
    training_file = os.path.join(cur_dir, training_file_name)
    generate_data(training_file,num_training_samples, do_print=True)
    test_file = os.path.join(cur_dir, test_file_name)
    generate_data(test_file,num_test_samples, do_print=True)
