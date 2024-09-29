CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Creating the metadata table with a hash-based id (using VARCHAR(64) for SHA-256)
CREATE TABLE metadata (
    id VARCHAR(64) PRIMARY KEY, 
    song_name VARCHAR(255) NOT NULL,
    album_name VARCHAR(255),
    release_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Foreign keys to related tables
    lyrics_id UUID REFERENCES lyrics(id)    -- FK to the lyrics table
);

-- Creating the lyrics table
CREATE TABLE lyrics (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    english_lyrics TEXT,
    telugu_lyrics TEXT
);

-- CREATE TABLE songs (
--     id SERIAL PRIMARY KEY,
--     song BYTEA,  -- The actual song file or URL reference
--     file_format VARCHAR(10)
-- );

-- CREATE TABLE bgm (
--     id SERIAL PRIMARY KEY,
--     bgm BYTEA,  -- BGM file or URL reference
--     file_format VARCHAR(10)
-- );

-- CREATE TABLE artists (
--     id SERIAL PRIMARY KEY,
--     artist_name VARCHAR(255) NOT NULL
-- );








---------------------------------------  Helper queries  ----------------------------------------------
-- For listing all the tables in the database.
-- SELECT table_name
-- FROM information_schema.tables
-- WHERE table_schema = 'public';

