import sys

from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

from kaleo.models import InvitationStat


class Command(BaseCommand):
    help = "Adds invites to all users with 0 invites remaining."
    
    def handle(self, *args, **kwargs):
        if len(args) == 0:
            sys.exit("You must supply the number of invites as an argument.")
        
        try:
            num_of_invites = int(args[0])
        except ValueError:
            sys.exit("The argument for number of invites must be an integer.")
        
        for user in User.objects.all():
            stat, _ = InvitationStat.objects.get_or_create(user=user)
            if stat.invites_remaining() == 0:
                stat.invites_allocated += num_of_invites
                stat.save()
