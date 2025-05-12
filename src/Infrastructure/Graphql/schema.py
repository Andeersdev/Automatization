from ariadne import gql

type_defs = gql(
"""
    type Response {
        status: String
        message: String
        data: String
    }

    input LoginInput {
        email: String
        password: String
        nickname: String
    }

    type Query {
        getAllUsers:Response
        getActiveUsers:Response
        getAllRoles:Response
        getActiveRoles:Response
        getRoleById(data: String!):Response
        getAllEnterprises:Response
        getActiveEnterprises:Response
    }

    type Mutation {
        login(data: LoginInput!): Response
        createUser(data: String!): Response
    } 
"""
)