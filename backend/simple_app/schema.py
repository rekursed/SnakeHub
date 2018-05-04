import graphene
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id

from . import models

class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        interfaces = (graphene.Node,)

class Query( graphene.AbstractType):
    # all_messages = graphene.List(MessageType)
    message = graphene.Field(MessageType , id = graphene.ID())
    def resolve_message(self,args,context,info):
        rid = from_global_id(args.get('id'))
        return models.Message.objects.get(pk=rid[1])
    #def resolve_all_messages(self,args , context, info):
    #    return models.Message.objects.all()
