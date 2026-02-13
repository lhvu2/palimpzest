import palimpzest as pz
from os.path import join
import os
import litellm

litellm._turn_on_debug()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current script directory: {script_dir}")

emails = pz.TextFileDataset(id="enron-emails", path=join(script_dir, "emails/"))
output = emails.run()

# filter for emails matching natural language criteria
emails = emails.sem_filter(
'The email includes the word Golf or golf or course',
)
# emails = emails.sem_filter(
# "The email contains a first-hand discussion of the business transaction",
# )

# # extract structured fields for each email
# emails = emails.sem_map([
# {"name": "subject", "type": str, "desc": "the subject of the email"},
# {"name": "sender", "type": str, "desc": "the email address of the sender"},
# {"name": "summary", "type": str, "desc": "a brief summary of the email"},
# ])

# execute the program and print the output
output = emails.run(max_quality=True)

print(output.to_df(cols=["filename", "sender", "subject", "summary"]))

pass