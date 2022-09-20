from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport



def gqlclient(imageurl,word,userid):

    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="http://localhost:8080/query")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query = gql('mutation createDiary{createDiary(input:{Userid:"%s",Imageurl:"%s",Word:"%s"}){Imageurl}}' % (userid,imageurl,word) )
    print(query)
    # a = "mutation createDiary{createDiary(input:{Userid:%s,Imageurl:%s,Word:%s}){Imageurl}}" % (userid,imageurl,word)

   

    # Execute the query on the transport
    result = client.execute(query)
    print(result)