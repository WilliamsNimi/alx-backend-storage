-- A script on MySQL Triggers
DROP TRIGGER IF EXISTS email_update;
DELIMITER &&
CREATE TRIGGER email_update AFTER UPDATE ON users
FOR EACH ROW
BEGIN
IF NEW.email != OLD.email THEN
SET valid_email = 0;
END IF;
END &&
DELIMITER;
