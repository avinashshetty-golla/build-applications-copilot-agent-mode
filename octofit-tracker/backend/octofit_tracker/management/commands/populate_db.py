from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), username='student1', email='student1@example.com', password='password1'),
            User(_id=ObjectId(), username='student2', email='student2@example.com', password='password2'),
            User(_id=ObjectId(), username='student3', email='student3@example.com', password='password3'),
        ]
        User.objects.bulk_create(users)

        # Debugging: Print user data to verify creation
        for user in User.objects.all():
            print(f"User: {user.username}, Email: {user.email}")

        # Create teams
        team = Team(_id=ObjectId(), name='Team A')
        team.save()
        team.members.add(*users)

        # Debugging: Print team data to verify creation
        for team in Team.objects.all():
            print(f"Team: {team.name}, Members: {[member.username for member in team.members.all()]}")

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Running', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Cycling', duration=timedelta(minutes=45)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Swimming', duration=timedelta(minutes=60)),
        ]
        Activity.objects.bulk_create(activities)

        # Debugging: Print activity data to verify creation
        for activity in Activity.objects.all():
            print(f"Activity: {activity.activity_type}, User: {activity.user.username}, Duration: {activity.duration}")

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Debugging: Print leaderboard data to verify creation
        for entry in Leaderboard.objects.all():
            print(f"Leaderboard: User: {entry.user.username}, Score: {entry.score}")

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Morning Run', description='A 5km run to start the day'),
            Workout(_id=ObjectId(), name='Cycling Session', description='A 20km cycling session'),
            Workout(_id=ObjectId(), name='Swimming Laps', description='30 minutes of lap swimming'),
        ]
        Workout.objects.bulk_create(workouts)

        # Debugging: Print workout data to verify creation
        for workout in Workout.objects.all():
            print(f"Workout: {workout.name}, Description: {workout.description}")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))