BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Users" (
	"User_id"	INTEGER,
	"Username"	TEXT NOT NULL UNIQUE,
	"Password"	TEXT NOT NULL,
	PRIMARY KEY("User_id")
);
CREATE TABLE IF NOT EXISTS "GameStates" (
	"GameStateID"	INTEGER,
	"UserID"	INTEGER,
	"DifficultyLevel"	TEXT,
	"SudokuBoard"	TEXT,
	"Notes"	TEXT,
	"StartTime"	TEXT,
	"EndTime"	TEXT,
	"IsCompleted"	INTEGER,
	PRIMARY KEY("UserID"),
	FOREIGN KEY("UserID") REFERENCES "Users"("User_id")
);
CREATE TABLE IF NOT EXISTS "HighScores" (
	"HighScoreID"	INTEGER,
	"UserID"	INTEGER,
	"DifficultyLevel"	TEXT,
	"CompletionTime"	INTEGER,
	PRIMARY KEY("HighScoreID"),
	FOREIGN KEY("UserID") REFERENCES "Users"("User_id")
);
CREATE TABLE IF NOT EXISTS "PuzzleBoard" (
	"PuzzleId"	INTEGER,
	"Puzzle"	TEXT,
	"Solution"	TEXT,
	"Difficulty"	TEXT,
	"Size"	INTEGER,
	PRIMARY KEY("PuzzleId")
);
COMMIT;
