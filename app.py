from flask import Flask
from flask_graphql import GraphQLView
import graphene
import csv

app = Flask(__name__)

class BankBranch(graphene.ObjectType):
    ifsc = graphene.String()
    branch = graphene.String()
    bank = graphene.String()

class Query(graphene.ObjectType):
    branches = graphene.List(BankBranch)

    def resolve_branches(self, info):
        data = []
        with open('bank_branches.csv', mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append({
                    'ifsc': row['ifsc'],
                    'branch': row['branch'],
                    'bank': row['bank_name']
                })
        return data

schema = graphene.Schema(query=Query)

# Create a GraphQL endpoint at /gql
app.add_url_rule('/gql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
