# Learning Django Rest Framework

In this, Djano Rest Framework has been used to make REST API calls. It supports both xml and json api format. It is a basic Online Voting System, where a user can create their own Political Parties and Vote 
for their parties. Any User can vote any party and can create a party.

## API LIST

Authentication
```
1. auth/login - POST - User Login
2. auth/register - POST -- User Signup
3. auth/logout - GET -- User Logout
```

Party
```
1. parties - GET - View All Parties
2. parties - POST - Create a Party
3. parties/{{party_id}} - GET - View A Party
4. parties/{{party_id}} - PUT - Delete A Party
```

Voting
```
1. votes - GET - View All Votes
2. votes - POST - Create a Vote
3. votes/{{vote_id}} - GET - View A Vote
4. votes/{{vote_id}} - PUT - Delete A Vote
```

## Installation Of Project

1. clone repository first
2. pip install -r requirement.txt

## Running Migration
```
python manage migrate -- This will migrate your all initial migrations
```