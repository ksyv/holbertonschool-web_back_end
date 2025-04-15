-- script that creates a stored procedure ComputeAverageScoreForUser 
-- that computes and store the average score for a student.
DELIMITER // 
CREATE PROCEDURE ComputeAverageScoreForUser (
    IN p_user_id INT 
)
BEGIN
    DECLARE v_average_score FLOAT;
    SELECT AVG(score) 
    INTO v_average_score 
    FROM corrections 
    WHERE user_id = p_user_id; 
    UPDATE users 
    SET average_score = v_average_score
    WHERE id = p_user_id;

END// 

DELIMITER ;
