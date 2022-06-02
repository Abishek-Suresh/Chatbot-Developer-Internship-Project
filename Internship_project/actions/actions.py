# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import mysql.connector
from typing import Any, Text, Dict, List
import re
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

def DataUpdate(name,email,phone_number,adults,children,room_type,room_num,check_in,check_out):
    mydb = mysql.connector.connect(
        host = "34.125.101.159",
        user = "root",
        passwrd = "2212",
        database = "Hotel_chatbot" 
    )

    mycursor = mydb.cursor()
    
    sql = 'INSERT INTO Booking_details (Name, Email, PhoneNumber, Adults_Staying, Children_Staying, RoomType, No_of_rooms_required, CheckIn_date, CheckOut_date) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}");'.format(name,email,phone_number,adults,children,room_type,room_num,check_in,check_out)
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "Record inserted successfully")


class ValidateBookRoomForm(FormValidationAction):
    def name(self) -> Text:
         return "validate_book_room_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name` value."""

        # Validating the name, what if it's short
        if len(slot_value) <=2:
            dispatcher.utter_message(text = f"That's a very short name. I'm assuming you mis-spelled.")
            return{"name": None}
        else:
            return{"name": slot_value}

       
    def validate_phone_number(
        self,
        slot_value:Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `phone_number` value."""
     # Validating the email
        if len(slot_value)==10:
            return{"phone_number": slot_value}
        else:
            dispatcher.utter_message(text = f"Your number is too short or too long.")
            return{"phone_number": None}

    def validate_email(
        self,
        slot_value:Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `email` value."""
     # Validating the email
        if ('@' not in slot_value) and (len(slot_value)<5) :
            dispatcher.utter_message(text = f"Your email ID isn't valid.")
            return{"email": None}
        else:
            return{"email": slot_value}

    def validate_check_in(
        self,
        slot_value:Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `check_in` value."""
     # Validating the check_in date
        if (re.search(r"\d{2}/\d{2}/\d{4}", slot_value)):
            return{"check_in": slot_value}
        else:
            dispatcher.utter_message(text = f"The entered date isn't valid one")
            return{"check_in": None}

    def validate_check_out(
        self,
        slot_value:Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `check_out` value."""
     # Validating the check_out date
        if (re.search(r"\d{2}/\d{2}/\d{4}", slot_value)):
            return{"check_out": slot_value}
        else:
            dispatcher.utter_message(text = f"The entered date isn't valid one")
            return{"check_out": None}
            
    
    
    
class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phone_number = tracker.get_slot("phone_number")
        adults = tracker.get_slot("adults")
        children = tracker.get_slot("children")
        room_type = tracker.get_slot("room_type")
        room_num = tracker.get_slot("room_num")
        check_in = tracker.get_slot("check_in")
        check_out = tracker.get_slot("check_out")

        dispatcher.utter_message(text= f"Full name of the registrant: {name}\n Email address: {email}\n Phone number: {phone_number}\n Number of adults staying: {adults}\n Number of children staying: {children}\n Room type: {room_type}\n Number of rooms: {room_num}\n Check-in date: {check_in}\n Check-out date: {check_out}\n Hotel front desk staff will contact the customer to exchange booking details. \n Thank you for trusting our hotel!")
        DataUpdate(name,email,phone_number,adults,children,room_type,room_num,check_in,check_out)
        return []




            
    