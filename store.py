from tkinter.messagebox import RETRY
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport



def gqlclient(imageurl,word,userid):
    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="https://watnow-362606.et.r.appspot.com/query")
    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)
    # Provide a GraphQL query
    query = gql('mutation createDiary{createDiary(input:{Userid:"%s",Imageurl:"%s",Word:"%s"}){Diaryid}}' % (userid,imageurl,word) )
    # a = "mutation createDiary{createDiary(input:{Userid:%s,Imageurl:%s,Word:%s}){Imageurl}}" % (userid,imageurl,word)
    # Execute the query on the transport
    result = client.execute(query)
    print(result["createDiary"]["Diaryid"])
    return result["createDiary"]["Diaryid"]

def createemotion(diaryid,happy,angry,fear,surprise,sad):
    # Select your transport with a defined url endpoint

    # 
    transport = AIOHTTPTransport(url="https://watnow-362606.et.r.appspot.com/query")
    # transport = AIOHTTPTransport(url="http://localhost:8080/query")
    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)
    # Provide a GraphQL query
    query = gql('mutation createEmotion{createEmotion(input:{Diaryid:"%s",Happy:"%s",Angry:"%s",Fear:"%s",Surprise:"%s",Sad:"%s"}){Diaryid}}' % (diaryid,happy,angry,fear,surprise,sad) )
    # a = "mutation createDiary{createDiary(input:{Userid:%s,Imageurl:%s,Word:%s}){Imageurl}}" % (userid,imageurl,word)
    # Execute the query on the transport
    result = client.execute(query)
    print(result)
    return result