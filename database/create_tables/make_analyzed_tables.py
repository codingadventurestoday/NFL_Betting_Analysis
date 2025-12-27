from database.connection import connect_to_db

conn = connect_to_db()
mycursor = conn.cursor()

"""
Table model_performance_teams
ID SMALLINT UNSIGNED PRIMARY KEY
teamID TINYINT FOREIGN KEY 
week TINYINT UNSIGNED
seasonID TINYINT UNSIGNED FOREIGN KEY
value {} TINYINT
type {MSE, REC, PRE, ACC, RSq, MAE} --> CHAR(3)

"""
"""
Table model_performance_NFL
ID SMALLINT UNSIGNED PRIMARY KEY
week TINYINT UNSIGNED
seasonID TINYINT UNSIGNED FOREIGN KEY
value {} TINYINT
type {MSE, REC, PRE, ACC, RSq, MAE} --> CHAR(3)
"""

create_performance_team = """
CREATE TABLE IF NOT EXISTS model_performance_teams (
    ID SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    teamID TINYINT UNSIGNED,
    seasonID TINYINT UNSIGNED,
    performance_value TINYINT,
    performance_type CHAR(3),
    predicted_game_type CHAR(4),
    FOREIGN KEY (teamID) REFERENCES teams(teamID),
    FOREIGN KEY (seasonID) REFERENCES seasons(seasonID)
    );
"""

create_performance_NFL = """
CREATE TABLE IF NOT EXISTS model_performance_NFL (
    ID SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    seasonID TINYINT UNSIGNED,
    performance_value TINYINT,
    performance_type CHAR(3),
    predicted_game_type CHAR(4),
    FOREIGN KEY (seasonID) REFERENCES seasons(seasonID)
    );
"""

mycursor.execute(create_performance_NFL)
mycursor.execute(create_performance_team)

conn.commit()

mycursor.close()
conn.close()
