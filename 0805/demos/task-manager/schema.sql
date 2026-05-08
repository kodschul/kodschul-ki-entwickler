-- TaskFlow schema
-- Run once at startup via db.func_init_db()

CREATE TABLE IF NOT EXISTS tasks (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    title      TEXT    NOT NULL,
    status     TEXT    NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP        DEFAULT CURRENT_TIMESTAMP
);
