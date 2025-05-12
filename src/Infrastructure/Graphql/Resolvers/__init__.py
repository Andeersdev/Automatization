from ariadne import QueryType, MutationType, make_executable_schema
from ..schema import type_defs
from ..Resolvers.AuthResolver import AuthResolver
from ..Resolvers.UserResolver import UserResolver
from ..Resolvers.RoleResolver import RoleResolver
from ..Resolvers.EnterpriseResolver import EnterpriseResolver

query = QueryType()
mutation = MutationType()

# Roles
query.set_field('getAllRoles', RoleResolver.resolve_get_all_roles)
query.set_field('getRoleById', RoleResolver.resolve_get_role_by_id)

# Enterprises
query.set_field('getAllEnterprises', EnterpriseResolver.resolve_get_all_enterprises)

# User
query.set_field('getAllUsers', UserResolver.resolve_get_all_users)
mutation.set_field('createUser', UserResolver.resolve_create_user)
# Auth
mutation.set_field('login', AuthResolver.resolve_login)

schema = make_executable_schema(type_defs, query, mutation)