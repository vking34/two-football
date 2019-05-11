### Report

+ Architecture Design:
	+ Client-Server
	+ Client: Flux
	+ Server: Passive MVC, Domain Driven Design, Onion


+ Brief API docs:

  + Sign up: 
    + POST /signup

  + Login: 
    + POST /login

  + Update profile (USER):
    + PUT /api/users/<user_id>

  + Deposit money into the balance of an account (USER):
    + POST /api/users/<user_id>/balance

  + Get all leagues: 
   	+ GET /api/v1/leagues

  + Add a league (ADMIN):
   	+ POST /api/v1/leagues

  + Get details of a league:
   	+ GET /api/v1/leagues/<league_id>

  + Update a league (ADMIN):
   	+ PUT /api/v1/leagues/<league_id>

  + Delete a league (ADMIN):
   	+ DELETE /api/v1/leagues/<league_id>

  + Get fixtures of matches filtered by start-date and stop-date | league_id:
   	+ GET /api/v1/matches?from=2019-03-15&to=2019-03-21&league_id=<league_id>

  + Get fixtures of a match:
   	+ GET /api/v1/matches/<match_id>

  + Comment on a match (USER):
  	+ POST /api/v1/matches/<match_id>/comments

	+ + Get comments of a match:
  	+ GET /api/v1/matches/<match_id>/comments

  + Bet on a match (USER):
   	+ POST /api/v1/matches/<match_id>/bets
		 
  + Millionaires ranking
    + GET /api/v1/users/millionaies
  

+ Details: 
	+ Content-Type: application/json

	+ Sign up for user:
    	+ POST /signup
    	+ Request Payload:
    		```
    		{
    		"username": "string",
    		"password": "string",
    		"name": "string",
    		"phone": "string",
    		"email": "string"
    		}
    		```

    	+ Responses:
    		+ OK:
    			+ Status Code: 200 
    			+ Payload:
    				```
    				{
    				"status" : true,
    				"user": {
    					"user_id": int,
    					"username": "string",
    					"name": "string",
    					"phone": "string",
    					"email": "string",
    					"balance": int,
    					"role": "string"
    					}
    				}
    				```
    		+ Bad request (Username is used already,...):
    			- Status Code: 400
    			- Payload:
    				```
    				{
    				"status": false,
    				"message": "string",
    				"code": int
    				}
    				```

    + Login:
    	- POST /login
    	- Request payload:
    		```
    		{
			"username": "string",
			"password": "string"
    		}
    		```
    	
    	- Responses:
    		+ OK:
    			- Status Code: 200
    			- Payload:
    				```
    				{
    				"status": true,
    				"access_token": "string",
    				"user": {
    					"user_id": int,
    					"username": "string",
    					"name": "string",
    					"phone": "string",
    					"email": "string",
    					"balance": int,
    					"role": "string"
    					}
    				}
    				```

    		+ Bad request (Username/password is wrong,...):
    			- Status Code: 400
    			- Payload:
    				```
    				{
    				"status": false,
    				"message": "string",
    				"code": int
    				}
    				```
	+ Update profile:
    	+ PUT /api/v1/users/<user_id>
    	+ Header: Authorization: Bearer TOKEN
    	+ Request Payload:
			```
			{
				"name": "string",
				"phone": "string",
				"email": "string"
			}
			```
		+ Responses:
    		+ OK:
        		+ Status Code: 200
        		+ Payload:
    				```
    				{
    				"status": true,
    				"user": {
    					"user_id": int,
    					"username": "string",
    					"name": "string",
    					"phone": "string",
    					"email": "string",
    					"balance": int,
    					"role": "string"
    					}
    				}
    				```
			+ Bad request (email is used already,...)
    			+ Status Code: 400
    			+ Payload:
    				```
    				{
    				"status": false,
    				"message": "string",
    				"code": int
    				}
    				```
	+ Deposit money into balance:
    	+ POST /api/v1/users/<user_id>/balance
    	+ Header: Authorization: Bearer TOKEN
    	+ Request Payload:
			```
			{
				"card_code": "string",
				"password": "string"
			}
			```
		+ Responses:
    		+ OK:
        		+ Status Code: 200
        		+ Payload:
					```
					{
						"status": true,
						"bill": 
						{
							"card_amount": int,
							"previous_balance": int,
							"balance": int,
							"deposit_time": "2019-03-22T20:00:00Z"
						}
					}
			+ Bad request (wrong card code):
    			+ Status Code: 400
    			+ Payload:
    				```
    				{
    				"status": false,
    				"message": "string",
    				"code": int
    				}
    				```				

    + Get leagues:
    	- GET /api/v1/leagues
    	- Responses:
    		+ OK:
        		- Status Code: 200
        		- Payload:
        			```
        			[
        				{
        				"league_id": int,
        				"league_name": "string",
        				"country": "string"
        				}
        			]
        			```
    
    + Add a league (ADMIN):
		+ POST /api/v1/leagues
		+ Header: Authorization: Bearer TOKEN
		+ Request Payload: 
			```
			{
				"league_id": int,
				"league_name": "string",
				"country": "string"
			}
			```
		+ Responses:
			+ OK:
				+ Status: 200
				+ Payload: 
					```
					{
						"status": true,
						"league":
								{
								"league_id": int,
								"league_name": "string",
								"country": "string"
								}
					}
					```
			
			+ Bad request (League exists, ...):
				+ Status Code: 400
				+ Payload:
					```
					{
					"status": false,
					"message": "string",
					"code": int
					}
					```
			+ Forbidden (User create league,...):
				+ Status Code: 403
				+ Payload:
					```
					{
					"status": false,
					"message": "string",
					"code": int
					}
					```

	+ Get a league:
		+ GET /api/v1/leagues/<league_id>
		+ Response:
			+ OK: 
				+ Status Code: 200
				+ Payload:
					```
					{
        				"league_id": int,
        				"league_name": "string",
        				"country": "string"
        			}
					```
	
	+ Update a league (ADMIN):
		+ PUT /api/v1/leagues/<league_id>
		+ Header: Authorization: Bearer TOKEN
		+ Request Payload: 
			```
			{
				"league_name": "string",
				"country": "string"
			}
			```
		+ Responses:
			+ OK:
				+ Status Code: 200
				+ Payload:
					```
					{
						"status": true,
						"league": {
							"league_id": int,
							"league_name": "string",
							"country": "string"
						}
					}
					```

			+ Bad request (name league is used already)
            	+ Status Code: 400
				+ Payload:
					```
					{
					"status": false,
					"message": "string",
					"code": int
					}
					```

	+ Delete a league (ADMIN):
		+ DELETE /api/v1/leagues/<league_id>
		+ Header: Authorization: Bearer TOKEN
		+ Responses:
    		+ OK:
            	+ Status: 200
            	+ Payload: 
            		```
    				{
    					"status": true,
    					"league":
    							{
    							"league_id": int,
    							"league_name": "string",
    							"country": "string"
    							}
    				}
  					```

			+ Bad request (League doesn't exist, ...):
    			+ Status Code: 400
    			+ Payload:
					```
					{
					"status": false,
					"message": "string",
					"code": int
					}
					```
    		+ Forbidden (User delete league,...):
    			+ Status Code: 403
      			+ Payload:
    				```
    				{
    				"status": false,
    				"message": "string",
    				"code": int
    				}
    				```

	+ Get fixtures of matches filtered by start-date and stop-date | league_id:
        + GET /api/v1/matches?from=2019-03-15&to=2019-03-21&league_id=<league_id>
        + Response:
          + OK:
            + Status Code: 200
            + Payload:
				```
				[
					{
						"match_id": int,
						"league_id": int,
						"match_date": "2019-03-20",
						"match_time": "15:00",
						"match_hometeam_name": "string",
						"match_awayteam_name": "string",
						"match_hometeam_halftime_score": int,
						"match_awayteam_halftime_score": int,
						"match_hometeam_score": int,
						"match_awayteam_score": int,
						"yellow_card": int
					}
				]
				```
	
	+ Get fixtures of a match:
        + GET /api/v1/matches/<match_id>
        + Response:
          + OK:
            + Status Code: 200
            + Payload:
				```
				{
					"match_id": int,
					"league_id": int,
					"match_date": "2019-03-20",
					"match_time": "15:00",
					"match_hometeam_name": "string",
					"match_awayteam_name": "string",
					"match_hometeam_halftime_score": int,
					"match_awayteam_halftime_score": int,
					"match_hometeam_score": int,
					"match_awayteam_score": int,
					"yellow_card": int
				}
				```
	
	+ Comment on a match (USER):
      + POST /api/v1/matches/<match_id>/comments
      + Header: Authorization: Bearer <user_token>
  		+ Request payload:
			```
			{
				"comment": "Goal!!!"
			}
			```
		+ Responses:
			+ OK:
				+ Status Code: 200
				+ Payload:
					```
					{
						"data": {
								"comment": "Goal!!!",
								"match_id": 410600,
								"time": "2019-05-11T16:22:18",
								"user_id": 10
						},
						"status": true
					}
					```
			+ Bad request:
				+ Status Code: 400
				+ Payload:
					```
						{
								"code": 602,
								"message": "Match not found",
								"status": false
						}
    				```
	+ Get comments of a match:
    	+ GET /api/v1/matches/<match_id>/comments
    	+ Params:
        	+ number: int		(get number of comments)
    	+ Response:
      	+ OK:
        	+ Status code: 200
        	+ Payload:
				```
						{
							"data": 
							[
								{
									"comment": "Goal!!!",
									"time": "2019-05-09T17:12:33",
									"user": {
										"name": "Dũng",
										"user_id": 10
									}
								},
								{
									"comment": "Messi hay nhưng không gánh đc team",
									"time": "2019-05-09T17:11:18",
									"user": {
										"name": "Dũng",
										"user_id": 10
									}
								}
							]
						}
				```

	+ Bet on a match (USER):
        + POST /api/v1/matches/<match_id>/bets
		+ Header: Authorization: Bearer TOKEN
		+ Request payload:
			```
			{
				"bet_type": 1,
				"bet_amount": 200,
				"bet_content": "2-1"
			}
			```
		+ Response:
			+ OK:
				+ Status Code:
				+ Payload:
				```
				{
					"bet": {
							"bet_amount": 200,
							"bet_content": "2-1",
							"bet_status": "PROCESSING",
							"bet_time": "2019-05-11T16:50:40",
							"bet_type": 1,
							"match_id": 413094,
							"user_id": 10
					},
					"status": true
				}
				```
			+ Bad request (Balance not enough,... ):
				+ Status Code: 400
				+ Payload:
					```
    				{
    				"status": false,
    				"message": "string",
    				"code": int
    				}
    				```

	+ Millionaires ranking
    	+ GET /api/v1/users/millionaies
		+ Responses:
			+ OK:
				+ Status Code: 200
				+ Payload:
					```
					[
						{
							"username": "string",
							"name": "string",
							"balance": int
						},
						{
							"username": "string",
							"name": "string",
							"balance": int
						}
					]
					```	
