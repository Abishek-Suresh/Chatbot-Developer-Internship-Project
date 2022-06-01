# Chatbot Project - Hotel Booking
This project is based on the Hotel booking business use case. Using the RASA framework, I’ve built a chatbot that can assist the consumer to book rooms. This chatbot can store the necessary information needed for booking a room, in a MySQL database. Also, it can answer frequently asked questions regarding the hotel. eg: About the available room types, contact number, canceling policy and canceling reservation info, etc.

## NLU.YML File :

In the nlu.yml file, I've created the following intents and provided appropriate examples for them.
<br>
The intents: 
* greet, 
* goodbye, 
* affirm, 
* deny, 
* mood_great, 
* mood_unhappy, 
* bot_challenge, 
* hotel_booking, 
* stop, 
* faq_check_in_time, 
* faq_checkout_time, 
* faq_cancel_policy, 
* faq_cancel_reservation, 
* faq_reception_time, 
* faq_parking, 
* faq_swimmingpool, 
* faq_wifi, rooms, 
* faq_contact_number, 
* thank you, 
* email_eg, 
* phone_num, 
* airport 
