/*
    COMP3311 24T1 Assignment 1
    IMDB Views, SQL Functions, and PlpgSQL Functions
    Student Name: <Your Name>
    Student ID: <Your ID>
*/

-- Question 1 --

/**
    Write a SQL View, called Q1, that:
    Retrieves the 10 movies with the highest number of votes.
*/
CREATE OR REPLACE VIEW Q1(Title, Year, Votes) AS
    -- TODO: Write your SQL query here
    SELECT
      mv.primary_title AS title,
      mv.release_year AS year,
      mv.votes
    FROM movies mv
    WHERE votes IS NOT NULL
    ORDER BY votes DESC
    LIMIT 10
;

-- Question 2 --

/**
    Write a SQL View, called Q2(Name, Title), that:
    Retrieves the names of people who have a year of death recorded in the database
    and are well known for their work in movies released between 2017 and 2019.
*/
CREATE OR REPLACE VIEW Q2(Name, Title) AS
    -- TODO: Write your SQL query here
    SELECT
      pp.name,
      mv.primary_title AS title
    FROM principals pr
    LEFT JOIN people pp ON pp.id = pr.person
    LEFT JOIN movies mv ON mv.id = pr.movie
    WHERE
      pp.death_year IS NOT NULL
      AND
      mv.release_year >= 2017
      AND
      mv.release_year <= 2019
    ORDER BY pp.name ASC
;

-- Question 3 *** --

/**
    Write a SQL View, called Q3(Name, Average), that:
    Retrieves the genres with an average rating not less than 6.5 and with more than 60 released movies.
*/
CREATE OR REPLACE VIEW Q3(Name, Average) AS
    -- TODO: Write your SQL query here
    SELECT
      gr.name,
      round(AVG(mv.score),2) as average
    FROM movies_genres mg
    LEFT JOIN genres gr ON gr.id = mg.genre
    LEFT JOIN movies mv ON mv.id = mg.movie
    -- WHERE
    --   mv.release_year IS NOT NULL
    GROUP BY gr.name
    HAVING
      COUNT(mv.*) > 60
      AND
      AVG(mv.score) > 6.5
    ORDER BY average DESC
;

-- Question 4 --

/**
    Write a SQL View, called Q4(Region, Average), that:
    Retrieves the regions with an average runtime greater than the average runtime of all movies.
*/
CREATE OR REPLACE VIEW Q4(Region, Average) AS
    -- TODO: Write your SQL query here
    SELECT
      rl.region,
      round(AVG(mv.runtime), 0) as average
    FROM
    (
      SELECT
        id, primary_title, runtime,
        AVG(runtime) OVER() as overall_average
      FROM movies
    ) mv
    LEFT JOIN releases rl ON rl.movie = mv.id
    GROUP BY mv.overall_average, rl.region
    HAVING overall_average < AVG(mv.runtime)
    ORDER BY average DESC, region ASC
;

-- Question 5 --

/**
    Write a SQL Function, called Q5(Pattern TEXT) RETURNS TABLE (Movie TEXT, Length TEXT), that:
    Retrieves the movies whose title matches the given regular expression,
    and displays their runtime in hours and minutes.
*/

CREATE OR REPLACE FUNCTION Q5(Pattern TEXT)
    RETURNS TABLE (Movie TEXT, Length Text)
    AS $$
        -- TODO: Write your SQL query here
        SELECT
          primary_title AS Movie,
          CASE
            WHEN runtime ISNULL THEN NULL
            ELSE CONCAT((runtime / 60)::TEXT, ' Hours ', (runtime % 60)::TEXT, ' Minutes')
          END AS Length
        FROM movies
        WHERE
          runtime IS NOT NULL
          AND
          primary_title LIKE CONCAT('%', Pattern, '%')
        ORDER BY primary_title ASC
        ;
    $$ LANGUAGE SQL
;

-- Question 6 --

/**
    Write a SQL Function, called Q6(GenreName TEXT) RETURNS TABLE (Year Year, Movies INTEGER), that:
    Retrieves the years with at least 10 movies released in a given genre.
*/
CREATE OR REPLACE FUNCTION Q6(GenreName TEXT)
    RETURNS TABLE (Year Year, Movies INTEGER)
    AS $$
        -- TODO: Write your SQL query here
        SELECT
          hp.year,
          hp.count AS movies
        FROM
        (
          SELECT
            gr.name,
            mv.release_year AS year,
            COUNT(mv.id)
          FROM movies_genres mg
          LEFT JOIN genres gr ON gr.id = mg.genre
          LEFT JOIN movies mv ON mv.id = mg.movie
          WHERE
            mv.release_year IS NOT NULL
          GROUP BY gr.name, mv.release_year
          HAVING COUNT(mv.id) > 10
        ) hp
        WHERE
          hp.name = GenreName
        ORDER BY movies DESC, hp.year DESC
      ;
    $$ LANGUAGE SQL
;

-- Question 7 *** --

/**
    Write a SQL Function, called Q7(MovieName TEXT) RETURNS TABLE (Actor TEXT), that:
    Retrieves the actors who have played multiple different roles within the given movie.
*/
CREATE OR REPLACE FUNCTION Q7(MovieName TEXT)
    RETURNS TABLE (Actor TEXT)
    AS $$
        -- TODO: Write your SQL query here
        SELECT
          pp.name AS Actor
        FROM roles r
        LEFT JOIN movies mv ON mv.id = r.movie
        LEFT JOIN people pp ON pp.id = r.person
        WHERE mv.primary_title = MovieName
        GROUP BY pp.name
        HAVING COUNT(r.played) > 1
        ORDER BY Actor ASC
        ;
    $$ LANGUAGE SQL
;

-- Question 8 *** --

/**
    Write a SQL Function, called Q8(MovieName TEXT) RETURNS TEXT, that:
    Retrieves the number of releases for a given movie.
    If the movie is not found, then an error message should be returned.
*/
CREATE OR REPLACE FUNCTION Q8(MovieName TEXT)
    RETURNS TEXT
    AS $$
    DECLARE	count TEXT;
    BEGIN
        -- TODO: Write your PLpgSQL function here
        SELECT count(*) INTO count
        FROM movies
        WHERE primary_title = MovieName
        ;

        IF (count = '0') THEN RETURN CONCAT('Movie ', '"', MovieName, '"', ' not found');
        END IF;

        SELECT count(*) INTO count
        FROM releases rl
        LEFT JOIN movies mv ON mv.id = rl.movie
        WHERE mv.primary_title = MovieName
        ;

        IF (count = '0') THEN RETURN CONCAT('No releases found for ', '"', MovieName, '"');
        END IF;

        -- !!!!!! The next line is correct !!!!!!
        -- RETURN CONCAT('Release count: ', count);
        -- !!!!!! The next line is just for VSCode issue workaround !!!!!!
        RETURN count;
    END
    $$ LANGUAGE PLpgSQL
;


-- Question 9 --

/**
    Write a SQL Function, called Q9(MovieName TEXT) RETURNS SETOF TEXT, that:
    Retrieves the Cast and Crew of a given movie.
*/
CREATE OR REPLACE FUNCTION Q9(MovieName TEXT)
    RETURNS SETOF TEXT
    AS $$
    BEGIN
        RETURN query
        -- TODO: Write your PLpgSQL function here

        SELECT CONCAT('"', name, '"', ' played ', '"', played, '"', ' in ', '"', title, '"')
        FROM
        (
          SELECT
            pp.name,
            mv.primary_title AS title,
            r.played
          FROM roles r
          LEFT JOIN movies mv ON mv.id = r.movie
          LEFT JOIN people pp ON pp.id = r.person
          WHERE mv.primary_title = MovieName
        )
        UNION
        SELECT CONCAT('"', name, '"', ' worked on ', '"', title, '"', ' as a ', profession)
        FROM
        (
          SELECT
            pp.name,
            mv.primary_title AS title,
            pf.name AS profession
          FROM credits c
          LEFT JOIN movies mv ON mv.id = c.movie
          LEFT JOIN people pp ON pp.id = c.person
          LEFT JOIN professions pf ON pf.id = c.profession
          WHERE
            pf.id <> 1 AND pf.id <> 7 AND pf.id <> 39
            AND
            mv.primary_title = MovieName
        )
        ;
    END
    $$ LANGUAGE PLpgSQL
;

-- Question 10 --

CREATE OR REPLACE VIEW Q10MovieGenre AS
  SELECT movie, string_agg(name, ', ') AS movie_genre
  FROM 
    (
      SELECT mg.movie, gr.name
      FROM movies_genres mg
      LEFT JOIN genres gr ON gr.id = mg.genre
      ORDER BY mg.movie, gr.name
    )
  GROUP BY movie
;

CREATE OR REPLACE VIEW Q10MoviePrincipal AS
  SELECT movie, string_agg(name, ', ') AS principals
  FROM 
    (
      SELECT pc.movie, pp.name
      FROM principals pc
      LEFT JOIN people pp ON pp.id = pc.person
      ORDER BY pc.movie, pp.name
    )
  GROUP BY movie
;

/**
    Write a PLpgSQL Function, called Q10(MovieRegion CHAR(4)) RETURNS TABLE (Year INTEGER, Best_Movie TEXT, Movie_Genre Text,Principals TEXT), that:
    Retrieves the list of must-watch movies for a given region, year by year.
*/
CREATE OR REPLACE FUNCTION Q10(MovieRegion CHAR(4))
    RETURNS TABLE (Year INTEGER, Best_Movie TEXT, Movie_Genre Text, Principals TEXT)
    AS $$
    BEGIN
        RETURN query
        -- TODO: Write your PLpgSQL function here

        SELECT
          -- region,
          release_year::INTEGER AS year,
          -- id,
          title AS best_movie,
          mg.movie_genre,
          mp.principals
        FROM
        (
          SELECT
            rl.region,
            mv.release_year,
            mv.id,
            mv.primary_title AS title,
            mv.score,
            MAX(mv.score) OVER(PARTITION BY rl.region, mv.release_year) as max
          FROM
          (
            SELECT region, movie
            FROM releases
            WHERE region = MovieRegion
            GROUP BY region, movie
          ) rl
          LEFT JOIN movies mv ON mv.id = rl.movie
        ) mvv
        LEFT JOIN Q10MovieGenre mg ON mg.movie = mvv.id
        LEFT JOIN Q10MoviePrincipal mp ON mp.movie = mvv.id
        WHERE score = max
        ORDER BY year DESC
        ;
    END
    $$ LANGUAGE PLpgSQL
;
