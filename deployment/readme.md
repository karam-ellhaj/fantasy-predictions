# This is the API endpoint for the machine learning model that predicts the points of the player in a match in fantasy
#### the model excpects those features to predict the player total-points

- position: Player's role on the field (e.g., forward, midfielder)
- assists: Number of times player set up goals
- bonus: Additional points awarded for outstanding performance
- clean_sheets: Matches where team conceded no goals
- goals_conceded: Number of goals allowed by player's team
- goals_scored: Number of goals scored by the player
- minutes: Time played by the player in minutes
- own_goals: Goals accidentally scored in player's own net
- penalties_missed: Number of penalty kicks not converted
- penalties_saved: Number of penalty kicks stopped by goalkeeper
- red_cards: Times player was sent off the field
- saves: Number of shots stopped by goalkeeper
- selected: Number of fantasy managers who chose player
- was_home: Whether the match was at home (true/false)
- yellow_cards: Number of cautions received by player
- GW: Gameweek number in the fantasy football season
- total_points_lag: Player's total points from previous gameweek