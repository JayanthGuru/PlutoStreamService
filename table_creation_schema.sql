CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE metadata_table (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    song_name VARCHAR(255) NOT NULL,
    album_name VARCHAR(255),
    release_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Foreign keys to related tables
    -- artist_id UUID  REFERENCES artists(id),                     -- FK to the songs table
    -- song_id UUID  REFERENCES songs(id) ON DELETE CASCADE,       -- FK to the songs table
    -- bgm_id UUID  REFERENCES bgm(id) ON DELETE CASCADE,          -- FK to the bgm table
    lyrics_id UUID  REFERENCES lyrics(id) ON DELETE CASCADE     -- FK to the lyrics table
);


-- Creating lyrics table
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

