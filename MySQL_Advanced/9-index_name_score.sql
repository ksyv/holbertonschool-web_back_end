-- script that want to 
-- create an index on two column
CREATE INDEX idx_name_first_score ON names (name(1), score);
