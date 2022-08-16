#twilio Pesada..ca1glor...!


from twilio.rest import Client 
 
account_sid = 'ACd1cd077bc00cdf38cd3befbbd3aa0e80' 
auth_token = '8eeaa455217992ea291279dc55e217d5' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(
							  from_='+12762849846',  
                              #messaging_service_sid='MGb442e709968ed997555cc3c1af38e965', 
                              body='Hello now',      
                              to='+351 ' 
                          ) 
 
print(message.sid)

