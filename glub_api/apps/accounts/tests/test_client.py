import json
from graphene_django.utils.testing import GraphQLTestCase


class TestUserCreation(GraphQLTestCase):
    def test_client_creation_mutation(self):
        variables = {
            "email": "ramoncito@gmail.com",
            "firstName": "Ramon",
            "lastName": "González",
            "birthday": "1992-10-09T00:00:00Z",
            "password": "123456",
            "username": "ramoncin"
        }
        response = self.query(
            '''
                mutation Register(
                    $email: String!,
                    $firstName: String!,
                    $lastName: String!,
                    $birthday: DateTime!,
                    $password: String!,
                    $username: String!
                ){
                  registerClient(
                                email: $email, 
                                firstName:$firstName, 
                                lastName:$lastName, 
                                birthday:$birthday, 
                                password:$password, 
                                username:$username){
                    user{
                      id
                      email
                            clientinfo{
                        birthday
                      }
                    }
                  }
                }
            ''',
            op_name='Register',
            variables=variables
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEquals(content["data"]["registerClient"]["user"]["email"], variables.get("email"))
