from twilio.rest import Client
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

account_sid=os.environ['ACCOUNT_SID']
auth_token=os.environ['AUTH_TOKEN']

client = Client(account_sid, auth_token)

client.messages.create(
    to="+16367515579",
    from_="+16362714878",
    body="Come on out on Memorial Day to Elco;  we want your business today!  reply to 636-751-5579",
    media_url="http://media5.picsearch.com/is?xenOyPFJcdmrH-z_kB5eZgtZQmi2tDltpwKqHTOVhDE&height=259")
