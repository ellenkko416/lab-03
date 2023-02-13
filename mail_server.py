from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
import uuid
import json


app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

# Function to load and save the mail to/from the json file

def load_mail() -> List[Dict[str, str]]:
    """
    Loads the mail from the json file

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    try:
        return json.loads(thisdir.joinpath('mail_db.json').read_text())
    except FileNotFoundError:
        return []

def save_mail(mail: List[Dict[str, str]]) -> None:
    """
    Summary: Saves a list of mails to a json file     
    Args:
    	mail(list): The list of dictionaries to concatenate with the json file 
    	
    Returns:
    	None
    
    """
    thisdir.joinpath('mail_db.json').write_text(json.dumps(mail, indent=4))

def add_mail(mail_entry: Dict[str, str]) -> str:
    """

    Summary: Adds mail to the json file 
    Args: 
    	mail_entry(dict): dictionary containing the mail to be added 
    
    Returns:
   	 string: unique identifier for the added mail
    """
    mail = load_mail()
    mail.append(mail_entry)
    mail_entry['id'] = str(uuid.uuid4()) # generate a unique id for the mail entry
    save_mail(mail)
    return mail_entry['id']

def delete_mail(mail_id: str) -> bool:
    """
    Summary: Deletes a mail entry from the json file
    Args:
    	mail_id(str): string containing the id of the mail that is to be deleted 
    Returns:
	bool: True if the mail entry was successfully deleted, false otherwise 
    """
    mail = load_mail()
    for i, entry in enumerate(mail):
        if entry['id'] == mail_id:
            mail.pop(i)
            save_mail(mail)
            return True

    return False

def get_mail(mail_id: str) -> Optional[Dict[str, str]]:
    """
    Summary:Gets a specific mail based on the specified mail id  
    Args:
    	mail_id(str) : contains mail id of desired mail to get
    Returns:
    	dict: if found, the mail that has the same id as the id taken as input 

    """
    mail = load_mail()
    for entry in mail:
        if entry['id'] == mail_id:
            return entry

    return None

def get_inbox(recipient: str) -> List[Dict[str, str]]:
    """
    Summary:Returns the inbox of the specified recipient 
    Args:
    	recipient(str): the recipient whose inbox will be returned 
    Return:
    	list: list of dictionaries containing all the mail in the inbox of the recipient 
    	
    """
    mail = load_mail()
    inbox = []
    for entry in mail:
        if entry['recipient'] == recipient:
            inbox.append(entry)

    return inbox

def get_sent(sender: str) -> List[Dict[str, str]]:
    """
    Summary:Gets all the mail sent by a specified sender
    Args:
    	sender(str): the desired sender 
    Return
    	list: list containing the dictionaries containing every email sent by the sender 
    """
    mail = load_mail()
    sent = []
    for entry in mail:
        if entry['sender'] == sender:
            sent.append(entry)

    return sent

# API routes - these are the endpoints that the client can use to interact with the server
@app.route('/mail', methods=['POST'])
def add_mail_route():
    """
    Summary: Adds a new mail entry to the json file
    Returns:
        str: The id of the new mail entry
    """
    mail_entry = request.get_json()
    mail_id = add_mail(mail_entry)
    res = jsonify({'id': mail_id})
    res.status_code = 201 # Status code for "created"
    return res

@app.route('/mail/<mail_id>', methods=['DELETE'])
def delete_mail_route(mail_id: str):
    """
    Summary: Deletes a mail entry from the json file
    Args:
        mail_id (str): The id of the mail entry to delete
    Returns:
        bool: True if the mail was deleted, False otherwise
    """
    del_mail = delete_mail(mail_id)
    if del_mail is True:
    	res = jsonify({'id':mail_id})
    	res.status_code = 200 # Status code for "ok"
    	return res
    else:
    	return('file not found')
    

@app.route('/mail/<mail_id>', methods=['GET'])
def get_mail_route(mail_id: str):
    """
    Summary: Gets a mail entry from the json file
    Args:
        mail_id (str): The id of the mail entry to get
    Returns:
        dict: A dictionary representing the mail entry if it exists, None otherwise
    """
    res = jsonify(get_mail(mail_id))
    res.status_code = 200 # Status code for "ok"
    return res

@app.route('/mail/inbox/<recipient>', methods=['GET'])
def get_inbox_route(recipient: str):
    """
    Summary: Gets all mail entries for a recipient from the json file
    Args:
        recipient (str): The recipient of the mail
    Returns:
        list: A list of dictionaries representing the mail entries
    """
    res = jsonify(get_inbox(recipient))
    res.status_code = 200
    return res

# TODO: implement a route to get all mail entries for a sender
# HINT: start with soemthing like this:
@app.route('/mail/sent/<sender>', methods=['GET'])
def get_sender_route(sender: str):
   """
   Summary: Gets the mails sent by a sender from the json file
   Args:
   	sender(str): the desired sender
   Returns:
   	list: list of dictionsries containing all the mail sent by the specified sender 
   
   """
   res = jsonify(get_sent(sender))
   res.status_code = 200
   return res


if __name__ == '__main__':
    app.run(port=5000, debug=True)
